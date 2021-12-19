from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.render.color_a import ColorA
from ascii_game.render.shader import SimpleShader, Shader
from ascii_game.render.texture import ObjectTexture
from ascii_game.vector import Vector3


@dataclass
class CameraComponent(Component):
    viewport: Vector3 = Vector3(8, 8, 8)
    default_rendered_shader: Shader = SimpleShader(ColorA(), ColorA(), ObjectTexture())
