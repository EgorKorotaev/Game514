from ascii_game.component import PhysicalComponent, GraphicComponent
from ascii_game.game_object import GameObject
from ascii_game.scene import Scene
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
            [[default_tile for x in range(map_range.x())] for y in range(map_range.y())]
            for z in range(map_range.z())
        ]
        self.map_default_position = map_default_position
        self.radius_tile = radius_view_tile


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
