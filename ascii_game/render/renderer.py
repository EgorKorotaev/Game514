from dataclasses import dataclass
from typing import cast

from ascii_game.render.camera import Camera
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.game_object import GameObject
from ascii_game.render.shader import RenderedTile
from ascii_game.scene import Scene


@dataclass
class TileView:
    pass


class Buffer:
    tile: list[list[RenderedTile]]

    def draw_tile(self, game_object: GameObject, camera: Camera):
        relative_tile_position = game_object.transform.position.to_2d() - camera.transform.position.to_2d()
        tile_is_in_viewport = (
            relative_tile_position.x < 0
            and relative_tile_position.y < 0
            or relative_tile_position.x > camera.viewport.x
            and relative_tile_position.y > camera.viewport.y
        )
        if tile_is_in_viewport:
            renderer_component = cast(RendererComponent, game_object.get_component(RendererComponent))
            underlying_tile = self.tile[relative_tile_position.y][relative_tile_position.x]
            rendered_tile = renderer_component.draw(underlying_tile, game_object.transform.position.z)
            self.tile[relative_tile_position.y][relative_tile_position.x] = rendered_tile


def render_scene(scene: Scene) -> Buffer:
    buffer = Buffer()

    camera = scene.get_camera()

    game_objects = scene.objects
    drawable_game_objects = get_drawable_game_objects(game_objects)

    drawable_game_objects.sort(key=lambda game_object: game_object.transform.position.z)

    for game_object in drawable_game_objects:
        buffer.draw_tile(game_object, camera)

    return buffer


def get_drawable_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererComponent) is not None]
