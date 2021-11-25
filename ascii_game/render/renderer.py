from dataclasses import dataclass
from typing import cast

from ascii_game.component.renderer_priority import RendererPriority
from ascii_game.render.camera import Camera
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.object.game_object import GameObject
from ascii_game.render.shader import RenderedTile, Shader, DefaultShader
from ascii_game.scene import Scene


@dataclass
class Buffer:
    tiles: list[list[list[list[GameObject]]]]
    rendered_tiles: list[list[RenderedTile]]

    def __init__(self, camera: Camera, shader: Shader = DefaultShader()):
        self.camera = camera
        self.tiles = [
            [[[] for x in range(camera.viewport.x)] for y in range(camera.viewport.y)] for z in range(camera.viewport.z)
        ]
        default_rendered_tile = shader.render(underlying_tile=None, position_z=0)
        self.rendered_tiles = [
            [default_rendered_tile for x in range(camera.viewport.x)] for y in range(camera.viewport.y)
        ]

    def add_game_object(self, game_object: GameObject):
        camera = self.camera
        relative_tile_position = game_object.transform.position - camera.transform.position
        tile_is_in_viewport = (
            relative_tile_position.z >= 0
            and relative_tile_position.y >= 0
            and relative_tile_position.x >= 0
            and relative_tile_position.z < camera.viewport.z
            and relative_tile_position.y < camera.viewport.y
            and relative_tile_position.x < camera.viewport.x
        )
        if tile_is_in_viewport:
            self.tiles[relative_tile_position.z][relative_tile_position.y][relative_tile_position.x].append(game_object)

    def draw_tiles(self):
        for z in range(len(self.tiles)):
            for y in range(len(self.tiles[z])):
                for x in range(len(self.tiles[z][y])):
                    if not len(self.tiles[z][y][x]):
                        continue

                    renderer_tile = max(
                        get_prioritized_game_objects(self.tiles[z][y][x]),
                        key=lambda i: i.get_component(RendererPriority).priority,
                    ).get_component(RendererComponent)
                    # renderer_tile = self.tiles[z][y][x][0].get_component(RendererComponent)
                    renderer_component = cast(RendererComponent, renderer_tile)
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
    # drawable_game_objects.sort(key=lambda game_object: game_object.transform.position.z)

    for game_object in drawable_game_objects:
        buffer.add_game_object(game_object)

    buffer.draw_tiles()

    return buffer


def get_drawable_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererComponent) is not None]


def get_prioritized_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererPriority) is not None]
