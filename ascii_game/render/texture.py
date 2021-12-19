from dataclasses import dataclass, field

from ascii_game.render.ansi_colored_text import ANSIColor
from ascii_game.render.color_a import ColorA


@dataclass
class BackgroundColor:
    color_id: ColorA = ColorA(a=0)


@dataclass
class ObjectColor:
    color_id: ColorA = ColorA(a=0)


@dataclass
class ObjectTexture:
    object_id: str = ""
