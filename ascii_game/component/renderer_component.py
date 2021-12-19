from dataclasses import dataclass, field

from ascii_game.component.component import Component
from ascii_game.render.shader import Shader, RenderedTile, SimpleShader
from ascii_game.vector import Vector3


@dataclass
class RendererComponent(Component):
    shader: Shader
    priority: int = 0

    def draw(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3) -> RenderedTile:
        return self.shader.render(underlying_tile, position_relative_to_camera)
