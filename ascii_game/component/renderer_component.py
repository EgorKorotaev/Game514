from ascii_game.renderer import TileView
from ascii_game.texture import DEFAULT_TILE_0


class RendererComponent:
    def __init__(self, texture: str = DEFAULT_TILE_0, color_modifier: str = ""):
        self.texture = texture
        self.color_modifier = color_modifier  # TODO class ColorModifier

    def draw(self) -> TileView:
        pass
