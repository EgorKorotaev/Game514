from dataclasses import dataclass

from ascii_game.primitive.color_a import ColorA


@dataclass
class BackgroundColor:
    color_id: ColorA = ColorA(a=0)


@dataclass
class ObjectColor:
    color_id: ColorA = ColorA(a=0)


@dataclass
class ObjectTexture:
    object_id: str = ""
