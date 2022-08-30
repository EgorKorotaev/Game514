import time
from dataclasses import dataclass
from typing import cast

from nagoya.component.camera_component import CameraComponent
from nagoya.component.renderer_component import RendererComponent
from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.object.game_object import GameObject
from nagoya.primitive.vector import Vector3
from nagoya.scene import Scene


@dataclass
class Buffer:
    tiles: list[list[list[GameObject]]]
    rendered_tiles: list[list[RenderedTile]]

    def __init__(self, camera: GameObject):
        self.camera_position = camera.transform.position
        camera_component = cast(CameraComponent, camera.get_component(CameraComponent))
        self.viewport = camera_component.viewport
        self.center = camera_component.center
        self.tiles = [[[] for x in range(self.viewport.x)] for y in range(self.viewport.y)]

        self.default_rendered_tile = camera_component.default_rendered_shader.render(underlying_tile=None)
        self.rendered_tiles = [
            [self.default_rendered_tile for x in range(self.viewport.x)] for y in range(self.viewport.y)
        ]

    def add_game_object(self, game_object: GameObject):
        x = game_object.transform.position.x - self.camera_position.x
        y = game_object.transform.position.y - self.camera_position.y
        z = game_object.transform.position.z - self.camera_position.z

        tile_is_in_viewport = (
            z >= 0 and y >= 0 and x >= 0 and z < self.viewport.z and y < self.viewport.y and x < self.viewport.x
        )
        if tile_is_in_viewport:
            self.tiles[y][x].append(game_object)

    def draw_tiles(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                if not len(self.tiles[y][x]):
                    continue

                self.tiles[y][x].sort(
                    key=lambda i: (i.transform.position.z, i.get_component(RendererComponent).priority)
                )
                rendered_tile = self.default_rendered_tile

                for i in range(len(self.tiles[y][x])):
                    rendered_object = self.tiles[y][x][i]
                    object_position = rendered_object.transform.position
                    x_from_camera = object_position.x - (self.center.x + self.camera_position.x)
                    y_from_camera = object_position.y - (self.center.y + self.camera_position.y)
                    z_from_camera = object_position.z - (self.center.z + self.camera_position.z)
                    rendered_tile = cast(RendererComponent, rendered_object.get_component(RendererComponent)).draw(
                        rendered_tile, Vector3(x=x_from_camera, y=y_from_camera, z=z_from_camera)
                    )

                self.rendered_tiles[y][x] = rendered_tile

    def test_draw_tiles(self):
        for y in range(len(self.tiles), 0, -1):
            for x in range(len(self.tiles[y])):
                if not len(self.tiles[y][x]):
                    continue

                self.tiles[y][x].sort(
                    key=lambda i: (i.transform.position.z, i.get_component(RendererComponent).priority)
                )
                rendered_tile = self.default_rendered_tile

                for i in range(len(self.tiles[y][x])):
                    rendered_object = self.tiles[y][x][i]
                    object_position = rendered_object.transform.position
                    x_from_camera = object_position.x - (self.center.x + self.camera_position.x)
                    y_from_camera = object_position.y - (self.center.y + self.camera_position.y)
                    z_from_camera = object_position.z - (self.center.z + self.camera_position.z)
                    rendered_tile = cast(RendererComponent, rendered_object.get_component(RendererComponent)).draw(
                        rendered_tile, Vector3(x=x_from_camera, y=y_from_camera, z=z_from_camera)
                    )

                self.rendered_tiles[y][x] = rendered_tile

    def print(self):
        for y in reversed(range(len(self.rendered_tiles))):
            for x in range(len(self.rendered_tiles[y])):
                printed_symbol = self.rendered_tiles[y][x].get_printed_symbol()
                print(printed_symbol, end="")
            print()


def render_scene(scene: Scene) -> Buffer:
    camera = scene.get_camera()
    buffer = Buffer(camera)

    game_objects = scene.game_objects()
    drawable_game_objects = get_drawable_game_objects(game_objects)

    for game_object in drawable_game_objects:
        buffer.add_game_object(game_object)

    buffer.draw_tiles()

    return buffer


def test_render_scene(scene: Scene) -> Buffer:
    camera = scene.get_camera()
    buffer = Buffer(camera)

    game_objects = scene.game_objects()
    drawable_game_objects = get_drawable_game_objects(game_objects)

    for game_object in drawable_game_objects:
        buffer.add_game_object(game_object)

    buffer.draw_tiles()

    return buffer


def get_drawable_game_objects(game_objects: list[GameObject]) -> list[GameObject]:
    return [game_object for game_object in game_objects if game_object.get_component(RendererComponent) is not None]
