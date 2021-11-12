from dataclasses import dataclass


@dataclass
class Point:
    x: int


@dataclass
class Vector2:
    x: int
    y: int

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)


@dataclass
class Vector3:
    x: int
    y: int
    z: int

    def to_2d(self):
        return Vector2(self.x, self.y)


@dataclass
class Vector4:
    x: int
    y: int
    z: int
    w: int
