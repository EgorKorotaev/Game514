from abc import ABC, abstractmethod

from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.primitive.vector import Vector3
from nagoya.shader.shader_visitor import ShaderVisitor


class Shader(ABC):
    @abstractmethod
    def render(
        self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None
    ) -> RenderedTile:
        pass

    @abstractmethod
    def accept(self, visitor: ShaderVisitor):
        pass
