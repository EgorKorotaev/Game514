from ascii_game.component.transform_component import TransformComponent
from ascii_game.game_object import GameObject, GameObjectId
from ascii_game.vector import Vector2


class Camera(GameObject):
    def __init__(self, viewport: Vector2 = Vector2(8, 8)):
        super().__init__()
        self.viewport = viewport
