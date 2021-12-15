from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from ascii_game.render.ansi_colored_text import colored_text, colored_background
from ascii_game.render.sty_colored_text import coloring_text_24bit, coloring_background_24bit
from ascii_game.render.texture import BackgroundColor, ObjectColor, ObjectTexture


@dataclass
class RenderedTile:
    background_color: BackgroundColor
    object_color: ObjectColor
    object_texture: ObjectTexture

    def get_printed_symbol(self) -> str:
        printed_symbol = ""

        if self.object_texture:
            printed_symbol = self.object_texture.object_id

        if self.object_color:
            printed_symbol = coloring_text_24bit(printed_symbol, self.object_color.color_id.get_rgb())

        if self.background_color:
            printed_symbol = coloring_background_24bit(printed_symbol, self.background_color.color_id.get_rgb())

        return printed_symbol


class Shader(ABC):
    @abstractmethod
    def render(self, underlying_tile: RenderedTile | None, position_z: int) -> RenderedTile:
        pass


@dataclass
class DefaultShader(Shader):
    background_color: BackgroundColor = field(default_factory=BackgroundColor)
    object_color: ObjectColor = field(default_factory=ObjectColor)
    object_texture: ObjectTexture = field(default_factory=ObjectTexture)

    def render(self, underlying_tile: RenderedTile | None, position_z: int) -> RenderedTile:
        return tile_mixing_default(
            RenderedTile(self.background_color, self.object_color, self.object_texture), underlying_tile
        )


def tile_mixing_default(tile: RenderedTile | None, underlying_tile: RenderedTile | None) -> RenderedTile | None:
    if not tile:
        return underlying_tile

    if not underlying_tile:
        return tile

    object_color = ObjectColor(underlying_tile.object_color.color_id + tile.object_color.color_id)
    object_texture = ObjectTexture(underlying_tile.object_texture.object_id + tile.object_texture.object_id)
    background_color = BackgroundColor(underlying_tile.background_color.color_id + tile.background_color.color_id)

    rendered_tile = RenderedTile(background_color, object_color, object_texture)
    return rendered_tile
