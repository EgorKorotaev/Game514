import colorsys
from copy import deepcopy
from dataclasses import dataclass

from ascii_game.visitor import PrimitiveVisitor


@dataclass
class ColorA:
    r: float = 0.00
    g: float = 0.00
    b: float = 0.00

    a: float = 1.00

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_color_a(self)

    def set_rgb(self, r: float, g: float, b: float):
        self.r, self.g, self.b = r, g, b

    def set_rgb_255(self, r: int, g: int, b: int):
        self.r, self.g, self.b = r / 255, g / 255, b / 255

    def set_hsl(self, h: float, s: float = 1, l: float = 0.5):
        self.r, self.g, self.b = colorsys.hls_to_rgb(h, l, s)

    def set_hsl_360(self, h: float, s: float = 100, l: float = 50):
        self.r, self.g, self.b = colorsys.hls_to_rgb(h, l, s)

    def get_rgb(self) -> (int, int, int):
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255))

    def get_hsl(self) -> (float, float, float):
        return colorsys.rgb_to_hls(self.r, self.g, self.b)

    def __add__(self, other):  # Не коммутативно
        color = deepcopy(self)
        color += other
        return color

    def __iadd__(self, other):
        r = other.r * other.a + self.r * self.a * (1 - other.a)
        g = other.g * other.a + self.g * self.a * (1 - other.a)
        b = other.b * other.a + self.b * self.a * (1 - other.a)
        a = other.a + self.a * (1 - other.a)

        self.r, self.g, self.b, self.a = r, g, b, a

        return self

    def lighten(self, percent):
        r = (1 - self.r) * percent + self.r
        g = (1 - self.g) * percent + self.g
        b = (1 - self.b) * percent + self.b
        return ColorA(r, g, b, a=self.a)

    def darken(self, percent):
        r = self.r - percent * self.r
        g = self.g - percent * self.g
        b = self.b - percent * self.b
        return ColorA(r, g, b, a=self.a)
