from dataclasses import dataclass

from ascii_game.visitor import PrimitiveVisitor


@dataclass
class Point:
    x: int = 0

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_point(self)


@dataclass
class Vector2:
    x: int = 0
    y: int = 0

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_vector2(self)

    def to_1d(self):
        return Point(self.x)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)


@dataclass
class Vector3:
    x: int = 0
    y: int = 0
    z: int = 0

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_vector3(self)

    def to_2d(self):
        return Vector2(self.x, self.y)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # def multiply(self, scalar: ):


@dataclass
class Vector4:
    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_vector4(self)

    def to_3d(self):
        return Vector3(self.x, self.y, self.z)
