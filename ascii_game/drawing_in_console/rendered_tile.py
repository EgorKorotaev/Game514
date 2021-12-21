from dataclasses import dataclass

from ascii_game.primitive.color_a import ColorA
from ascii_game.drawing_in_console.sty_colored_text import coloring_text_24bit, coloring_background_24bit
from ascii_game.render.texture import ObjectTexture


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