from dataclasses import dataclass

from ascii_game.game_object import GameObject
from ascii_game.render.camera import Camera


@dataclass
class Scene:
    objects: list[GameObject]
    camera_id: int

    def __init__(self):
        self.objects = [Camera()]
        self.camera_id = 0

    def get_camera(self) -> Camera | None:
        camera = self.objects[self.camera_id]
        if not isinstance(camera, Camera):
            # camera_ids = list[filter(lambda camera: isinstance(camera, Camera), self.objects)]
            for object_id in range(len(self.objects)):
                if isinstance(self.objects[object_id], Camera):
                    camera = self.objects[object_id]
        return camera

    def add_object(self, game_object: GameObject):
        self.objects.append(game_object)
