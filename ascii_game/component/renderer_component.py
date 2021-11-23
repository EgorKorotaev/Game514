from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.render.shader import Shader, RenderedTile
from ascii_game.render.material import Material, DefaultMaterial


@dataclass
class RendererComponent(Component):
    material: Material = DefaultMaterial()  # TODO add defaults shader

    def set_shader(self, shader: Shader):
        self.material.shader = shader

    def draw(self, underlying_tile: RenderedTile, position_z: int) -> RenderedTile:
        return self.material.render(underlying_tile, position_z)
