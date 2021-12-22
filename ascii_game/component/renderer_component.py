from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.drawing_in_console.rendered_tile import RenderedTile
from ascii_game.visitor import ComponentVisitor
from ascii_game.shader.shader import Shader
from ascii_game.primitive.vector import Vector3


class RendererComponent(Component):
    def __init__(self, game_object: "GameObject", shader: Shader, priority: int = 0):
        super().__init__(game_object)
        self.shader = shader
        self.priority = priority

    def draw(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3) -> RenderedTile:
        return self.shader.render(underlying_tile, position_relative_to_camera)

    def accept(self, visitor: ComponentVisitor):
        return visitor.visit_renderer(self)

    def init(self) -> None:
        pass
