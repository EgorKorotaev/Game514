from dataclasses import dataclass
from ascii_game.test_print_map import Scene
from ascii_game.vector import Vector3, Vector2


@dataclass
class TileView:
    pass


class Buffer:
    tile: list[list[list[TileView]]]

    def draw_tile(self, tile: TileView, coord: Vector2, z, camera):
        if coord.x < 0 and coord.y < 0 or coord.x > camera.vision.x and coord.y > camera.vision.y:
            self.tile[coord.x][coord.y][z] = tile  # TODO адщфе → ште
            # TODO сначала причесать
            # TODO потом мёрдж столбиков


def render_scene(self, scene: Scene) -> Buffer:
    buffer = Buffer()

    camera = scene.camera

    objects = scene.get_objects()
    for object in objects:
        buffer.draw_tile(
            object.graphicObject.draw(),
            object.transform.position.to_2d() - camera.position.to_2d(),
            object.transform.position.z,
            camera
        )

    return buffer
