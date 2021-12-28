from nagoya.component import CameraComponent, Component, KeyboardSubjectComponent, RendererComponent, \
    TransformComponent, CustomComponent
from nagoya.object.game_object import GameObject

from .load_primitive import load_vector3
from .load_shader import load_shader
from nagoya.component.custom_component import get_component


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
        case _:
            return _load_custom_component(game_object, component)


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


def _load_custom_component(game_object: GameObject, component: dict) -> CustomComponent:
    return get_component(component["type"]).load_from_json(game_object, component['fields'])
