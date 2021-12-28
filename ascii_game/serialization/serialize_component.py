from ascii_game.component.camera_component import CameraComponent
from ascii_game.component.component import Component
from ascii_game.component.keyboard_subject_component import KeyboardSubjectComponent
from ascii_game.component.renderer_component import RendererComponent
from ascii_game.component.transform_component import TransformComponent
from ascii_game.game.player_controller import PlayerController
from ascii_game.serialization.serialize_primitive import serialize_vector3
from ascii_game.serialization.serialize_shader import serialize_shader
from ascii_game.visitor import ComponentVisitor


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
            "priority": element.priority,
        }

    def visit_transform(self, element: TransformComponent) -> None:
        self.serialized_component = {"type": "TransformComponent", "position": serialize_vector3(element.position)}

    def visit_player_controller(self, element: PlayerController) -> None:
        self.serialized_component = {"type": "PlayerController"}
