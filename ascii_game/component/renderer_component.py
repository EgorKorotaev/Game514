from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.render.shader import Shader, RenderedTile, DefaultShader


@dataclass
class RendererComponent(Component):
    shader: Shader = DefaultShader()  # TODO add defaults shader

    def set_shader(self, shader: Shader):
        self.shader = shader

    def draw(self, underlying_tile: RenderedTile, position_z: int) -> RenderedTile:
        return self.shader.render(underlying_tile, position_z)
