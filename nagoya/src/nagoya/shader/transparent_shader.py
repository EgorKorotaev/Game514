from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.primitive import ColorA
from nagoya.primitive.vector import Vector3
from nagoya.render.texture import ObjectTexture

from .shader import Shader
from .shader_visitor import ShaderVisitor


class TransparentShader(Shader):
    def __init__(self, color: ColorA):
        self.color = color

    def render(
        self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None
    ) -> RenderedTile:
        if underlying_tile is None:
            return RenderedTile(
                background_color=self.color, object_color=ColorA(0, 0, 0, a=0), object_texture=ObjectTexture()
            )

        background_color = underlying_tile.background_color + self.color
        object_color = underlying_tile.object_color + self.color

        return RenderedTile(
            background_color=background_color, object_color=object_color, object_texture=underlying_tile.object_texture
        )

    def accept(self, visitor: ShaderVisitor):
        return visitor.visit_transparent(self)

    @staticmethod
    def create_transparent_shader(color: ColorA = ColorA()) -> "TransparentShader":
        return TransparentShader(color)
