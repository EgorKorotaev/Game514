from ascii_game.texture import DEFAULT_TILE_0
from ascii_game.vector import Vector3


class PhysicalComponent:
    def __init__(self, map_range: Vector3 = Vector3(1, 1, 1)):
        self.map_range = map_range


class GraphicComponent:
    def __init__(self, texture: str = DEFAULT_TILE_0, color_modifier: str = ""):
        self.texture = texture
        self.color_modifier = color_modifier  # TODO class ColorModifier
