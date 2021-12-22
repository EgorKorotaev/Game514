from dataclasses import dataclass
from typing import cast

from ascii_game.component.keyboard_subject_component import create_keyboard_subject
from ascii_game.object.game_object import GameObject
from ascii_game.render.camera import create_camera


@dataclass
class Scene:
    _objects: list[GameObject]
    camera_id: int
    keyboard_subject_id: int

    def __init__(self, objects: list[GameObject], camera_id: int, keyboard_subject_id: int):
        self._objects = objects
        self.camera_id = camera_id
        self.keyboard_subject_id = keyboard_subject_id

    def game_objects(self) -> list[GameObject]:
        return self._objects

    def get_camera(self) -> GameObject:
        camera = self._objects[self.camera_id]
        return cast(GameObject, camera)

    def add_object(self, game_object: GameObject):
        self._objects.append(game_object)

    @staticmethod
    def create_scene() -> "Scene":
        return Scene([create_camera(), create_keyboard_subject()], 0, 1)
