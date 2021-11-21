from dataclasses import dataclass

from ascii_game.component.component import Component
from ascii_game.render.renderer import TileView
from ascii_game.texture import DEFAULT_TILE_0


@dataclass
class RendererComponent(Component):
    texture: str = DEFAULT_TILE_0
    color_modifier: str = ""

    def draw(self) -> TileView:
        pass
