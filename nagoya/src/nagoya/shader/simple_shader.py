from nagoya.drawing_in_console.rendered_tile import RenderedTile
from nagoya.primitive import ColorA
from nagoya.primitive.vector import Vector3
from nagoya.render.texture import ObjectTexture

from .shader import Shader
from .shader_visitor import ShaderVisitor


class SimpleShader(Shader):
    def __init__(self, background_color: ColorA, object_color: ColorA, object_texture: ObjectTexture):
        self.background_color = background_color
        self.object_color = object_color
        self.object_texture = object_texture

    def render(
        self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None
    ) -> RenderedTile:
        this_tile = RenderedTile(self.background_color, self.object_color, self.object_texture)

        if underlying_tile is None:
            return this_tile

        self.adjust_color_to_height(this_tile, position_relative_to_camera.z)
        tile_mixed = self.mix_tiles(underlying_tile, this_tile)

        return tile_mixed

    def mix_tiles(self, underlying_tile: RenderedTile | None, tile: RenderedTile | None) -> RenderedTile | None:
        background_color = underlying_tile.background_color + tile.background_color
        object_color = tile.object_color
        object_texture = tile.object_texture

        if tile.object_texture.object_id == "":
            object_texture = underlying_tile.object_texture
            object_color = underlying_tile.object_color

        rendered_tile = RenderedTile(background_color, object_color, object_texture)

        return rendered_tile

    def adjust_color_to_height(self, tile: RenderedTile, delta_z: int):
        viewport = 4
        percent = abs(delta_z / viewport)
        match delta_z:
            case _ if delta_z == 0:
                return
            case _ if delta_z < 0:
                tile.background_color = tile.background_color.darken(percent)
                tile.object_color = tile.object_color.darken(percent)
            case _ if delta_z > 0:
                tile.background_color = tile.background_color.lighten(percent)
                tile.object_color = tile.object_color.lighten(percent)

    def accept(self, visitor: ShaderVisitor):
        return visitor.visit_simple(self)

    @staticmethod
    def create_simple_shader(
        background_color: ColorA = ColorA(),
        object_color: ColorA = ColorA(),
        object_texture: ObjectTexture = ObjectTexture(),
    ) -> "SimpleShader":
        return SimpleShader(background_color, object_color, object_texture)
