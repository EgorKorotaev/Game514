from ascii_game.object.game_object import GameObject
from ascii_game.vector import Vector2


class Camera(GameObject):
    def __init__(self, viewport: Vector2 = Vector2(8, 8)):
        super().__init__()  # transform x:0 y:0 z:0
        self.viewport = viewport
