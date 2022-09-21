import numpy as np
import time
from dataclasses import dataclass
from typing import cast

from nagoya.component.camera_component import CameraComponent
from nagoya.component.renderer_component import RendererComponent
from nagoya.object.game_object import GameObject
from nagoya.scene import Scene


@dataclass
class GifBuffer:
    tiles: list[list[list[list[GameObject]]]]
    rendered_tiles: np.ndarray

    def __init__(self, camera: GameObject):
        self.camera_position = camera.transform.position
        camera_component = cast(CameraComponent, camera.get_component(CameraComponent))
        self.viewport = camera_component.viewport
        self.center = camera_component.center
        self.tiles = [
            [[[] for z in range(self.viewport.z)] for x in range(self.viewport.x)] for y in range(self.viewport.y)
        ]

        self.default_rendered_tile = camera_component.default_rendered_shader.render(underlying_tile=None)
        # TODO Потом вынести в конфиг ассетов или куда-то дальше
        self.rendered_tiles = np.array([
            [(0 * 255, 0 * 255, 0 * 255, 0 * 255) for x in range(24 + (self.viewport.x - 1) * 12 + (self.viewport.y - 1) * 12)]
            for y in range(24 + (self.viewport.x - 1) * 6 + (self.viewport.y - 1) * 6 + (self.viewport.z - 1) * 13)
        ])
        self.offset_z = self.viewport.z - 1
        self.offset_y = self.viewport.y - 1
        self.offset_x = self.viewport.x - 1

    def add_game_object(self, game_object: GameObject):
        x = game_object.transform.position.x - self.camera_position.x
        y = game_object.transform.position.y - self.camera_position.y
        z = game_object.transform.position.z - self.camera_position.z

        tile_is_in_viewport = (
                z >= 0 and y >= 0 and x >= 0 and z < self.viewport.z and y < self.viewport.y and x < self.viewport.x
        )
        if tile_is_in_viewport:
            self.tiles[y][x][z].append(game_object)

    def draw_tiles(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                for z in range(len(self.tiles[y][x])):
                    if not len(self.tiles[y][x][z]):
                        continue

                    _y_start = x * 6 + y * 6 + (self.offset_z - z) * 13
                    _x_start = x * 12 + (self.offset_y - y) * 12

                    self.tiles[y][x][z].sort(key=lambda i: i.get_component(RendererComponent).priority)

                    sprite = cast(
                        RendererComponent,
                        self.tiles[y][x][z][0].get_component(RendererComponent)
                    ).sprite
                    height, withe, count_color = sprite.shape

                    for _y in range(height):
                        for _x in range(withe):
                            if sprite[_y][_x][3] != 0:
                                self.rendered_tiles[_y + _y_start][_x + _x_start] = sprite[_y][_x]


def render_scene(scene: Scene) -> GifBuffer:
    camera = scene.get_camera()
    buffer = GifBuffer(camera)

    game_objects = scene.game_objects()
    drawable_game_objects = get_drawable_game_objects(game_objects)

    for game_object in drawable_game_objects:
        buffer.add_game_object(game_object)

    started = time.time()
    buffer.draw_tiles()
    print("Took %0.3fs" % (time.time() - started))

    return buffer


def get_drawable_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererComponent) is not None]
