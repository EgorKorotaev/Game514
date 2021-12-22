from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.visitor import ComponentVisitor
from ascii_game.primitive.color_a import ColorA
from ascii_game.shader.shader import Shader
from ascii_game.shader.simple_shader import SimpleShader
from ascii_game.render.texture import ObjectTexture
from ascii_game.primitive.vector import Vector3


@dataclass
class CameraComponent(Component):
    viewport: Vector3 = Vector3(8, 8, 8)
    default_rendered_shader: Shader = SimpleShader(ColorA(), ColorA(), ObjectTexture())

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_camera(self)

    def update(self, subject) -> None:
        pass
