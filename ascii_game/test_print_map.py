from ascii_game.component import PhysicalComponent, GraphicComponent
from ascii_game.game_object import GameObject
from ascii_game.vector import Point, Vector3


class LogicLevelMap:  # TODO достаточно отражается сущьность обхекта?
    def __init__(
        self,
        map_range: Vector3 = Vector3(16, 16, 16),
        default_tile: GameObject = GameObject(PhysicalComponent(), GraphicComponent()),
        map_default_position: Vector3 = Vector3(8, 8, 4),
        radius_view_tile: Point = Point(1),  # TODO куда этот параметр?
    ):

        self.map = [
            [
                [default_tile for x in range(map_range.x())]
                for y in range(map_range.y())
            ]
            for z in range(map_range.z())
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
        self.objects: dict[str, GameObject] = {}
        self.logicLevelMap = logicLevelMap
        self.camera = camera
        self.camera.position = self.logicLevelMap.map_default_position

    def rendering(self):
        objects = self.objects
        r = self.logicLevelMap.radius_tile.x()
        z_start = self.camera.position.z()
        z_end = self.camera.vision.z()
        y_start = self.camera.position.y()
        y_end = self.camera.vision.y()
        x_start = self.camera.position.x()
        x_end = self.camera.vision.x()

        raw_render_map = []

        return raw_render_map

    @staticmethod
    def camera_is_out_of_map_range(map, x, y, z):
        camera_is_out_of_map_range = False
        if z < len(map):
            if y < len(map[z]):
                if x < len(map[z][y]):
                    camera_is_out_of_map_range = True
        return camera_is_out_of_map_range

    def get_objects(self) -> list[GameObject]:
        pass


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
