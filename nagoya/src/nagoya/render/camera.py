from nagoya.component.camera_component import CameraComponent
from nagoya.object.game_object import GameObject


def create_camera() -> GameObject:
    camera = GameObject.create_game_object()
    camera.add_component(CameraComponent.create_camera_component(camera))
    return camera
