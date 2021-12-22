from dataclasses import dataclass

from ascii_game.drawing_in_console.rendered_tile import RenderedTile
from ascii_game.visitor import ShaderVisitor
from ascii_game.primitive.color_a import ColorA
from ascii_game.shader.shader import Shader
from ascii_game.render.texture import ObjectTexture
from ascii_game.primitive.vector import Vector3


@dataclass
class SimpleShader(Shader):
    background_color: ColorA
    object_color: ColorA
    object_texture: ObjectTexture

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

        rendered_tile = RenderedTile(background_color, object_color, object_texture)

        return rendered_tile

    def adjust_color_to_height(self, tile: RenderedTile, delta_z: int):
        viewport = 10
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