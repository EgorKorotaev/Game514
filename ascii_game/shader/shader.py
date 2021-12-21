from abc import ABC, abstractmethod

from ascii_game.drawing_in_console.rendered_tile import RenderedTile
from ascii_game.visitor import ShaderVisitor
from ascii_game.primitive.vector import Vector3


class Shader(ABC):
    @abstractmethod
    def render(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None) -> RenderedTile:
        pass

    @abstractmethod
    def accept(self, visitor: ShaderVisitor):
        pass
