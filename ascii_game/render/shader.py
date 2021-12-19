from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from ascii_game.render.color_a import ColorA
from ascii_game.render.sty_colored_text import coloring_text_24bit, coloring_background_24bit
from ascii_game.render.texture import BackgroundColor, ObjectColor, ObjectTexture
from ascii_game.vector import Vector3


@dataclass
class RenderedTile:
    background_color: ColorA
    object_color: ColorA
    object_texture: ObjectTexture = ObjectTexture()

    def get_printed_symbol(self) -> str:
        printed_symbol = ""

        if self.object_texture:
            printed_symbol = self.object_texture.object_id

        if self.object_color:
            printed_symbol = coloring_text_24bit(printed_symbol, self.object_color.get_rgb())

        if self.background_color:
            printed_symbol = coloring_background_24bit(printed_symbol, self.background_color.get_rgb())

        return printed_symbol


class Shader(ABC):
    @abstractmethod
    def render(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None) -> RenderedTile:
        pass


@dataclass
class SimpleShader(Shader):
    background_color: ColorA
    object_color: ColorA
    object_texture: ObjectTexture

    def render(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None) -> RenderedTile:
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

        if tile.object_texture.object_id == '':
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


@dataclass
class TransparentShader(Shader):
    color: ColorA

    def render(self, underlying_tile: RenderedTile | None, position_relative_to_camera: Vector3 | None = None) -> RenderedTile:
        if underlying_tile is None:
            return RenderedTile(background_color=self.color, object_color=ColorA(0, 0, 0, a=0), object_texture=ObjectTexture())

        background_color = underlying_tile.background_color + self.color
        object_color = underlying_tile.object_color + self.color

        return RenderedTile(background_color=background_color, object_color=object_color, object_texture=underlying_tile.object_texture)
