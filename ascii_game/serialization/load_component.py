from ascii_game.component.camera_component import CameraComponent
from ascii_game.component.component import Component
from ascii_game.component.keyboard_subject_component import KeyboardSubjectComponent
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.component.transform_component import TransformComponent
from ascii_game.game.player_controller import PlayerController
from ascii_game.object.game_object import GameObject
from ascii_game.serialization.load_primitive import load_vector3
from ascii_game.serialization.load_shader import load_shader


def load_component(game_object: GameObject, component: dict) -> Component:
    match component["type"]:
        case "CameraComponent":
            return _load_camera_component(game_object, component)
        case "KeyboardSubjectComponent":
            return _load_keyboard_subject(game_object, component)
        case "RendererComponent":
            return _load_renderer_component(game_object, component)
        case "TransformComponent":
            return _load_transform_component(game_object, component)
        case "PlayerController":
            return _load_player_controller(game_object, component)


def _load_camera_component(game_object: GameObject, component: dict) -> CameraComponent:
    return CameraComponent(
        game_object=game_object,
        viewport=load_vector3(component["viewport"]),
        default_rendered_shader=load_shader(shader=component["default_rendered_shader"]),
    )


def _load_keyboard_subject(game_object: GameObject, component: dict) -> KeyboardSubjectComponent:
    return KeyboardSubjectComponent(game_object=game_object)


def _load_renderer_component(game_object: GameObject, component: dict) -> RendererComponent:
    return RendererComponent(
        game_object=game_object, shader=load_shader(component["shader"]), priority=component["priority"]
    )


def _load_transform_component(game_object: GameObject, component: dict) -> TransformComponent:
    return TransformComponent(game_object=game_object, position=load_vector3(component["position"]))


def _load_player_controller(game_object: GameObject, component: dict) -> PlayerController:
    return PlayerController(game_object)
