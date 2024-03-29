from auvers_game.game.player_controller import PlayerController
from nagoya.component import (
    CameraComponent,
    Component,
    ComponentVisitor,
    KeyboardSubjectComponent,
    RendererComponent,
    TransformComponent,
    CustomComponent,
)

from .serialize_primitive import serialize_vector3
from .serialize_shader import serialize_shader
from .serialize_sprite import serialize_sprite


def serialize_component(component: Component) -> dict:
    json_component_visitor = JSONExportComponentVisitor()
    component.accept(json_component_visitor)
    return json_component_visitor.serialized_component


class JSONExportComponentVisitor(ComponentVisitor):
    def __init__(self):
        self.serialized_component: dict = {}

    def visit_camera(self, element: CameraComponent) -> None:
        self.serialized_component = {
            "type": "CameraComponent",
            "viewport": serialize_vector3(element.viewport),
            "center": serialize_vector3(element.center),
            "default_rendered_shader": serialize_shader(element.default_rendered_shader),
        }

    def visit_keyboard_subject(self, element: KeyboardSubjectComponent) -> None:
        self.serialized_component = {
            "type": "KeyboardSubjectComponent",
        }

    def visit_renderer(self, element: RendererComponent) -> None:
        self.serialized_component = {
            "type": "RendererComponent",
            "shader": serialize_shader(element.shader),
            "sprite": serialize_sprite(element.sprite),
            "priority": element.priority,
        }

    def visit_transform(self, element: TransformComponent) -> None:
        self.serialized_component = {"type": "TransformComponent", "position": serialize_vector3(element.position)}

    def visit_custom_component(self, element: CustomComponent) -> None:
        self.serialized_component = {"type": element.__name__, "fields": element.params_to_json()}
