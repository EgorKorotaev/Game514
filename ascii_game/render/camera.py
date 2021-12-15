from ascii_game.component.camera_component import CameraComponent
from ascii_game.object.game_object import GameObject


def create_camera() -> GameObject:
    camera = GameObject()
    camera.add_component(CameraComponent())
    return camera
