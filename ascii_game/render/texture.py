from dataclasses import dataclass, field

from ascii_game.render.colored_text import ANSIColor


@dataclass
class BackgroundColor:
    color_id: ANSIColor | str = field(default_factory=str)


@dataclass
class ObjectColor:
    color_id: ANSIColor | str = field(default_factory=str)


@dataclass
class ObjectTexture:
    object_id: ANSIColor | str = field(default_factory=str)
