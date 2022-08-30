import time
from dataclasses import dataclass
from typing import cast

from nagoya.component.camera_component import CameraComponent
from nagoya.component.renderer_component import RendererComponent
from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.object.game_object import GameObject
from nagoya.primitive.vector import Vector3
from nagoya.scene import Scene
from nagoya.shader.shader import Shader


@dataclass
class Buffer2:
    tiles: list[list[list[list[GameObject]]]]
    rendered_tiles: list[list[RenderedTile]]

    def __init__(self, camera: GameObject):
        self.camera_position = camera.transform.position
        camera_component = cast(CameraComponent, camera.get_component(CameraComponent))
        self.viewport = camera_component.viewport
        self.center = camera_component.center
        self.tiles = [
            [[[] for z in range(self.viewport.z)] for x in range(self.viewport.x)] for y in range(self.viewport.y)
        ]

        self.default_rendered_tile = camera_component.default_rendered_shader.render(underlying_tile=None)
        self.rendered_tiles = [
            [self.default_rendered_tile for x in range(self.viewport.x * 2 + self.viewport.y + 1)]
            for y in range(self.viewport.y + self.viewport.z + 1)
        ]
        self.offset_z = self.viewport.z
        self.offset_y = self.viewport.y
        self.offset_x = self.viewport.x

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
        for y in range(len(self.tiles) - 1, 0, -1):
            # for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                #     for x in range(len(self.tiles[y]) - 1, 0, -1):
                if y > 1 and x < len(self.tiles[y]) - 1:
                    # if y - 1 < len(self.tiles):
                    #     if not len(self.tiles[y - 1][0][0]):
                    #         break

                    rendered_object = []
                    __z = 0

                    for _z in range(len(self.tiles[y][x]) - 1, 0, -1):
                        if not len(self.tiles[y][x][_z]):
                            continue
                        if len(rendered_object):
                            break
                        rendered_object = self.tiles[y][x][_z]
                        __z = _z

                    rendered_object.sort(key=lambda i: (i.get_component(RendererComponent).priority))

                    if not len(rendered_object):
                        continue

                    background_color_a = cast(
                        RendererComponent,
                        rendered_object[0].get_component(RendererComponent)
                    ).shader.background_color.a

                    if background_color_a == 1 or True:
                        _y = y + __z
                        _x = x * 2 + y
                        if _y < 0 or _x < 0:
                            continue
                        rendered_tile_0 = self.rendered_tiles[_y][_x]
                        rendered_tile_1 = self.rendered_tiles[_y + 1][_x]
                        rendered_tile_2 = self.rendered_tiles[_y + 1][_x + 1]
                        rendered_tile_3 = self.rendered_tiles[_y + 1][_x + 2]
                        rendered_tile_4 = self.rendered_tiles[_y][_x + 2]
                        rendered_tile_5 = self.rendered_tiles[_y][_x + 1]

                        for i in range(len(self.tiles[y][x][__z])):
                            rendered_object = self.tiles[y][x][__z][i]
                            object_position = rendered_object.transform.position
                            z_from_camera = object_position.z - (self.center.z + self.camera_position.z)
                            rendered_tile_0 = cast(
                                RendererComponent, rendered_object.get_component(RendererComponent)
                            ).draw(rendered_tile_0, Vector3(x=0, y=1, z=z_from_camera))
                            rendered_tile_1 = cast(
                                RendererComponent, rendered_object.get_component(RendererComponent)
                            ).draw(rendered_tile_1, Vector3(x=0, y=0, z=z_from_camera))
                            rendered_tile_2 = cast(
                                RendererComponent, rendered_object.get_component(RendererComponent)
                            ).draw(rendered_tile_2, Vector3(x=1, y=0, z=z_from_camera))
                            rendered_tile_3 = cast(
                                RendererComponent, rendered_object.get_component(RendererComponent)
                            ).draw(rendered_tile_3, Vector3(x=2, y=0, z=z_from_camera))
                            rendered_tile_4 = cast(
                                RendererComponent, rendered_object.get_component(RendererComponent)
                            ).draw(rendered_tile_4, Vector3(x=2, y=1, z=z_from_camera))
                            rendered_tile_5 = cast(
                                RendererComponent, rendered_object.get_component(RendererComponent)
                            ).draw(rendered_tile_5, Vector3(x=1, y=1, z=z_from_camera))

                        self.rendered_tiles[_y][_x] = rendered_tile_0
                        self.rendered_tiles[_y + 1][_x] = rendered_tile_1
                        self.rendered_tiles[_y + 1][_x + 1] = rendered_tile_2
                        self.rendered_tiles[_y + 1][_x + 2] = rendered_tile_3
                        self.rendered_tiles[_y][_x + 2] = rendered_tile_4
                        self.rendered_tiles[_y][_x + 1] = rendered_tile_5
                        continue

                for z in range(len(self.tiles[y][x])):
                    if not len(self.tiles[y][x][z]):
                        continue

                    # _y = y + z + self.offset_z
                    # _x = x * 2 - y + self.offset_y
                    _y = y + z
                    _x = x * 2 + y
                    if _y < 0 or _x < 0:
                        continue

                    self.tiles[y][x][z].sort(key=lambda i: (i.get_component(RendererComponent).priority))

                    rendered_tile_0 = self.rendered_tiles[_y][_x]
                    rendered_tile_1 = self.rendered_tiles[_y + 1][_x]
                    rendered_tile_2 = self.rendered_tiles[_y + 1][_x + 1]
                    rendered_tile_3 = self.rendered_tiles[_y + 1][_x + 2]
                    rendered_tile_4 = self.rendered_tiles[_y][_x + 2]
                    rendered_tile_5 = self.rendered_tiles[_y][_x + 1]

                    for i in range(len(self.tiles[y][x][z])):
                        rendered_object = self.tiles[y][x][z][i]
                        object_position = rendered_object.transform.position
                        z_from_camera = object_position.z - (self.center.z + self.camera_position.z)
                        rendered_tile_0 = cast(
                            RendererComponent, rendered_object.get_component(RendererComponent)
                        ).draw(rendered_tile_0, Vector3(x=0, y=1, z=z_from_camera))
                        rendered_tile_1 = cast(
                            RendererComponent, rendered_object.get_component(RendererComponent)
                        ).draw(rendered_tile_1, Vector3(x=0, y=0, z=z_from_camera))
                        rendered_tile_2 = cast(
                            RendererComponent, rendered_object.get_component(RendererComponent)
                        ).draw(rendered_tile_2, Vector3(x=1, y=0, z=z_from_camera))
                        rendered_tile_3 = cast(
                            RendererComponent, rendered_object.get_component(RendererComponent)
                        ).draw(rendered_tile_3, Vector3(x=2, y=0, z=z_from_camera))
                        rendered_tile_4 = cast(
                            RendererComponent, rendered_object.get_component(RendererComponent)
                        ).draw(rendered_tile_4, Vector3(x=2, y=1, z=z_from_camera))
                        rendered_tile_5 = cast(
                            RendererComponent, rendered_object.get_component(RendererComponent)
                        ).draw(rendered_tile_5, Vector3(x=1, y=1, z=z_from_camera))

                    self.rendered_tiles[_y][_x] = rendered_tile_0
                    self.rendered_tiles[_y + 1][_x] = rendered_tile_1
                    self.rendered_tiles[_y + 1][_x + 1] = rendered_tile_2
                    self.rendered_tiles[_y + 1][_x + 2] = rendered_tile_3
                    self.rendered_tiles[_y][_x + 2] = rendered_tile_4
                    self.rendered_tiles[_y][_x + 1] = rendered_tile_5

    def print(self):
        for y in reversed(range(len(self.rendered_tiles))):
            for x in range(len(self.rendered_tiles[y])):
                printed_symbol = self.rendered_tiles[y][x].get_printed_symbol()
                print(printed_symbol, end="")
            print()


def render_scene2(scene: Scene) -> Buffer2:
    camera = scene.get_camera()
    buffer = Buffer2(camera)

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
