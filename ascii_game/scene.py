from dataclasses import dataclass
from typing import cast

from ascii_game.object.game_object import GameObject
from ascii_game.render.camera import Camera


@dataclass
class Scene:
    objects: list[GameObject]
    camera_id: int

    def __init__(self):
        self.objects = [Camera()]  # transform x:0 y:0 z:0
        self.camera_id = 0

    def get_camera(self) -> Camera:
        camera = self.objects[self.camera_id]
        return cast(Camera, camera)

    def add_object(self, game_object: GameObject):
        self.objects.append(game_object)
