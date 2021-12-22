from ascii_game.component.camera_component import CameraComponent
from ascii_game.component.component import Component
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.component.transform_component import TransformComponent
from ascii_game.serialization.load_primitive import load_vector3


def load_component(component: dict) -> Component:
    match component['type']:
        case 'TransformComponent':
            return load_transform_component(component)
        case 'CameraComponent':
            return load_camera_component(component)
        case 'RendererComponent':
            return load_renderer_component(component)


def load_transform_component(component: dict) -> TransformComponent:
    return TransformComponent(position=load_vector3(component['position']))


def load_camera_component(component: dict) -> CameraComponent:
    pass


def load_renderer_component(component: dict) -> RendererComponent:
    pass
