import colorsys
from dataclasses import dataclass


@dataclass
class ColorA:
    r: float = 0.00
    g: float = 0.00
    b: float = 0.00

    h: float = 0.00
    s: float = 0.00
    l: float = 0.00

    a: float = 1.00

    def set_rgb(self, r: float, g: float, b: float):
        self.r, self.g, self.b = r, g, b
        self.h, self.l, self.s = colorsys.rgb_to_hls(r, g, b)

    def set_rgb_255(self, r: int, g: int, b: int):
        self.r, self.g, self.b = r / 255, g / 255, b / 255
        self.h, self.l, self.s = colorsys.rgb_to_hls(r, g, b)

    def set_hsl(self, h: float, s: float = 1, l: float = 0.5):
        self.h, self.l, self.s = h, l, s
        self.r, self.g, self.b = colorsys.hls_to_rgb(h, l, s)

    def set_hsl_360(self, h: float, s: float = 100, l: float = 50):
        self.h, self.l, self.s = h / 360, l / 100, s / 100
        self.r, self.g, self.b = colorsys.hls_to_rgb(h, l, s)

    def get_rgb(self) -> (int, int, int):
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255))

    def get_hsl(self) -> (float, float, float):
        return (self.h, self.s, self.l)

    def __add__(self, other):
        r = other.r * other.a + self.r * self.a * (1 - other.a)
        g = other.g * other.a + self.g * self.a * (1 - other.a)
        b = other.b * other.a + self.b * self.a * (1 - other.a)
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        a = other.a + self.a * (1 - other.a)
        color = ColorA(r, g, b, h, l, s, a)
        return color
