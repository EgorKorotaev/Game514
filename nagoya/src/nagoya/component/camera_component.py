from nagoya.object.game_object import GameObject
from nagoya.primitive.vector import Vector3
from nagoya.shader.shader import Shader
from nagoya.shader.simple_shader import SimpleShader

from .component import Component
from .component_visitor import ComponentVisitor


class CameraComponent(Component):
    def __init__(self, game_object: GameObject, viewport: Vector3, default_rendered_shader: Shader):
        super().__init__(game_object)
        self.viewport = viewport
        self.default_rendered_shader = default_rendered_shader

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_camera(self)

    def init(self) -> None:
        pass

    @staticmethod
    def create_camera_component(game_object: GameObject) -> "CameraComponent":
        return CameraComponent(
            game_object=game_object,
            viewport=Vector3(8, 8, 8),
            default_rendered_shader=SimpleShader.create_simple_shader(),
        )
