from ascii_game.component.transform_component import TransformComponent
from ascii_game.game_object import GameObject, GameObjectId
from ascii_game.vector import Vector3


class Camera(GameObject):
    def __init__(self, game_object_id: GameObjectId, viewport: Vector3 = Vector3(8, 8, 1)):
        super().__init__(game_object_id=game_object_id)
        self.viewport = viewport
