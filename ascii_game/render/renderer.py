from dataclasses import dataclass
from typing import cast

from ascii_game.component.camera_component import CameraComponent
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.object.game_object import GameObject
from ascii_game.render.shader import RenderedTile, Shader, DefaultShader
from ascii_game.scene import Scene


@dataclass
class Buffer:
    tiles: list[list[list[list[GameObject]]]]
    rendered_tiles: list[list[RenderedTile]]

    def __init__(self, camera: GameObject, shader: Shader = DefaultShader()):
        self.camera_position = camera.transform.position
        self.viewport = cast(CameraComponent, camera.get_component(CameraComponent)).viewport
        self.tiles = [
            [[[] for x in range(self.viewport.x)] for y in range(self.viewport.y)] for z in range(self.viewport.z)
        ]
        default_rendered_tile = shader.render(underlying_tile=None, position_z=0)
        self.rendered_tiles = [[default_rendered_tile for x in range(self.viewport.x)] for y in range(self.viewport.y)]

    def add_game_object(self, game_object: GameObject):
        relative_tile_position = game_object.transform.position - self.camera_position
        tile_is_in_viewport = (
            relative_tile_position.z >= 0
            and relative_tile_position.y >= 0
            and relative_tile_position.x >= 0
            and relative_tile_position.z < self.viewport.z
            and relative_tile_position.y < self.viewport.y
            and relative_tile_position.x < self.viewport.x
        )
        if tile_is_in_viewport:
            self.tiles[relative_tile_position.z][relative_tile_position.y][relative_tile_position.x].append(game_object)

    def draw_tiles(self):
        for z in range(len(self.tiles)):
            for y in range(len(self.tiles[z])):
                for x in range(len(self.tiles[z][y])):
                    if not len(self.tiles[z][y][x]):
                        continue

                    tile_renderer = max(
                        self.tiles[z][y][x],
                        key=lambda i: i.get_component(RendererComponent).priority,
                    ).get_component(RendererComponent)

                    renderer_component = cast(RendererComponent, tile_renderer)
                    underlying_tile = self.rendered_tiles[y][x]
                    rendered_tile = renderer_component.draw(underlying_tile, z)
                    self.rendered_tiles[y][x] = rendered_tile

    def print(self):
        for y in range(len(self.rendered_tiles)):
            for x in range(len(self.rendered_tiles[y])):
                printed_symbol = self.rendered_tiles[y][x].get_printed_symbol()
                print(printed_symbol, end="")
            print()


def render_scene(scene: Scene) -> Buffer:
    camera = scene.get_camera()
    buffer = Buffer(camera)

    game_objects = scene.objects
    drawable_game_objects = get_drawable_game_objects(game_objects)

    for game_object in drawable_game_objects:
        buffer.add_game_object(game_object)

    buffer.draw_tiles()

    return buffer


def get_drawable_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererComponent) is not None]
