from ascii_game.object.game_object import GameObject
from ascii_game.vector import Vector3


class Camera(GameObject):
    def __init__(self, viewport: Vector3 = Vector3(8, 8, 4)):
        self.viewport = viewport
        super().__init__()  # transform x:0 y:0 z:0
