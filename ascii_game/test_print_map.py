from ascii_game.component import PhysicalComponent, GraphicComponent
from ascii_game.game_object import GameObject
from ascii_game.vector import Vector1, Vector3


class LogicLevelMap:  # TODO достаточно отражается сущьность обхекта?
    def __init__(
        self,
        map_range: Vector3 = Vector3(16, 16, 16),
        default_tile: GameObject = GameObject(PhysicalComponent(), GraphicComponent()),
        map_default_position: Vector3 = Vector3(8, 8, 4),
        radius_view_tile: Vector1 = Vector1(1),  # TODO куда этот параметр?
    ):

        self.map = [
            [
                [default_tile for x in range(map_range.get_int_x())]
                for y in range(map_range.get_int_y())
            ]
            for z in range(map_range.get_int_z())
        ]
        self.map_default_position = map_default_position
        self.radius_tile = radius_view_tile


class Camera:
    def __init__(
        self,
        vision: Vector3 = Vector3(8, 8, 1),
        position: Vector3 = Vector3(0, 0, 0),  # TODO куда этот параметр?
    ):
        self.vision = vision
        self.position = position


class Scene:
    def __init__(
        self, logicLevelMap: LogicLevelMap = LogicLevelMap(), camera: Camera = Camera()
    ):
        self.logicLevelMap = logicLevelMap
        self.camera = camera
        self.camera.position = self.logicLevelMap.map_default_position

    # TODO ПРОДОЛЖИТЬ ТУТ!
    #  Сделать промежуточное смешение по z, и потом рендер.
    #  И добавить заголовки x, y, z
    def rendering(self):
        map = self.logicLevelMap.map
        r = self.logicLevelMap.radius_tile.get_int_x()
        z_start = self.camera.position.get_int_z()
        z_end = self.camera.vision.get_int_z()
        y_start = self.camera.position.get_int_y()
        y_end = self.camera.vision.get_int_y()
        x_start = self.camera.position.get_int_x()
        x_end = self.camera.vision.get_int_x()

        # for z in range(z_start, z_start + z_end):
        for z in range(z_start + z_end, z_start + z_end + 1):
            for rz in range(r):  # TODO Не нужно. Скорее всего
                for y in range(y_start, y_start + y_end):
                    for ry in range(r):
                        for x in range(x_start, x_start + x_end):
                            for rx in range(r):
                                print(map[z][y][x].graphicObject.texture, end=" ")
                        print()

    def info_rendering(self):
        map = self.logicLevelMap.map
        r = self.logicLevelMap.radius_tile.get_int_x()
        z_start = self.camera.position.get_int_z()
        z_end = self.camera.vision.get_int_z()
        y_start = self.camera.position.get_int_y()
        y_end = self.camera.vision.get_int_y()
        x_start = self.camera.position.get_int_x()
        x_end = self.camera.vision.get_int_x()

        raw_render_map = []

        # for z in range(z_start, z_start + z_end):
        for z in range(z_start, z_start + 1):
            raw_render_map.append([])
            for rz in range(r):

                for y in range(y_start, y_start + y_end + 1):
                    raw_render_map[z - z_start].append([])
                    for ry in range(r):

                        for x in range(x_start, x_start + x_end + 1):
                            raw_render_map[z - z_start][y - y_start].append([])
                            for rx in range(r):

                                if self.camera_is_out_of_map_range(map, x, y, z):
                                    if y == y_start:
                                        if x != x_start:
                                            texture = str(x - 1).rjust(2, "_")
                                            game_object = GameObject(
                                                PhysicalComponent(),
                                                GraphicComponent(texture=texture),
                                            )
                                            raw_render_map[z - z_start][y - y_start][
                                                x - x_start
                                            ] = game_object
                                        else:
                                            texture = "  "
                                            game_object = GameObject(
                                                PhysicalComponent(),
                                                GraphicComponent(texture=texture),
                                            )
                                            raw_render_map[z - z_start][y - y_start][
                                                x - x_start
                                            ] = game_object
                                    if y != y_start:
                                        if x == x_start:
                                            texture = str(y - 1).rjust(2, "_")
                                            game_object = GameObject(
                                                PhysicalComponent(),
                                                GraphicComponent(texture=texture),
                                            )
                                            raw_render_map[z - z_start][y - y_start][
                                                x - x_start
                                            ] = game_object
                                        else:
                                            raw_render_map[z - z_start][y - y_start][
                                                x - x_start
                                            ] = map[z][y][x]
                                else:
                                    texture = ""
                                    game_object = GameObject(
                                        PhysicalComponent(),
                                        GraphicComponent(texture=texture),
                                    )
                                    raw_render_map[z - z_start][y - y_start][
                                        x - x_start
                                    ] = game_object

        for z in range(1, len(raw_render_map)):
            for rz in range(r):
                for y in range(1, len(raw_render_map[z])):
                    for ry in range(r):
                        for x in range(1, len(raw_render_map[z][y])):
                            for rx in range(r):
                                camera_is_out_of_map_range = False
                                if y < len(map):
                                    if x < len(map[y]):
                                        camera_is_out_of_map_range = True

                                if camera_is_out_of_map_range:
                                    raw_render_map[z][y][x] = map[z][y][x]

        return raw_render_map

    @staticmethod
    def camera_is_out_of_map_range(map, x, y, z):
        camera_is_out_of_map_range = False
        if z < len(map):
            if y < len(map[z]):
                if x < len(map[z][y]):
                    camera_is_out_of_map_range = True
        return camera_is_out_of_map_range


def main():
    scene = Scene()
    rendering_3d_matrix(scene.info_rendering())


def rendering_2d_matrix(matrix: list[list[GameObject]]):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print(matrix[y][x].graphicObject.texture, end=" ")
        print()


def rendering_3d_matrix(matrix: list[list[list[GameObject]]]):
    for z in range(len(matrix)):
        for y in range(len(matrix[z])):
            for x in range(len(matrix[z][y])):
                print(matrix[z][y][x].graphicObject.texture, end=" ")
            print()


if __name__ == "__main__":
    main()
