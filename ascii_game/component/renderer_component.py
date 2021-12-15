from dataclasses import dataclass, field

from ascii_game.component.component import Component
from ascii_game.render.shader import Shader, RenderedTile, DefaultShader


@dataclass
class RendererComponent(Component):
    shader: Shader = field(default_factory=DefaultShader)
    priority: int = 0

    def draw(self, underlying_tile: RenderedTile, position_z: int) -> RenderedTile:
        return self.shader.render(underlying_tile, position_z)
