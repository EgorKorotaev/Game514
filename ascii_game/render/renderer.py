from dataclasses import dataclass
from typing import cast

from ascii_game.render.camera import Camera
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.object.game_object import GameObject
from ascii_game.render.material import DefaultMaterial, Material
from ascii_game.render.shader import RenderedTile, Shader, DefaultShader
from ascii_game.scene import Scene


@dataclass
class Buffer:
    tiles: list[list[RenderedTile]]

    def __init__(self, camera: Camera, material: Material = DefaultMaterial()):
        self.camera = camera
        default_rendered_tile = material.render(underlying_tile=None, position_z=0)
        self.tiles = [
            [default_rendered_tile for x in range(camera.transform.position.x)]
            for y in range(camera.transform.position.y)
        ]

    def draw_tile(self, game_object: GameObject):
        camera = self.camera
        relative_tile_position = game_object.transform.position.to_2d() - camera.transform.position.to_2d()
        tile_is_in_viewport = (
            relative_tile_position.x < 0
            and relative_tile_position.y < 0
            or relative_tile_position.x > camera.viewport.x
            and relative_tile_position.y > camera.viewport.y
        )
        if tile_is_in_viewport:
            renderer_component = cast(RendererComponent, game_object.get_component(RendererComponent))
            underlying_tile = self.tiles[relative_tile_position.y][relative_tile_position.x]
            rendered_tile = renderer_component.draw(underlying_tile, game_object.transform.position.z)
            self.tiles[relative_tile_position.y][relative_tile_position.x] = rendered_tile


def render_scene(scene: Scene) -> Buffer:
    camera = scene.get_camera()
    buffer = Buffer(camera)

    game_objects = scene.objects
    drawable_game_objects = get_drawable_game_objects(game_objects)
    drawable_game_objects.sort(key=lambda game_object: game_object.transform.position.z)

    for game_object in drawable_game_objects:
        buffer.draw_tile(game_object)

    return buffer


def get_drawable_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererComponent) is not None]
