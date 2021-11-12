from ascii_game.vector import Vector3


class PhysicalComponent:
    def __init__(self, map_range: Vector3 = Vector3(1, 1, 1)):
        self.map_range = map_range


