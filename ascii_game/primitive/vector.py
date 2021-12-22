from copy import deepcopy
from dataclasses import dataclass

from ascii_game.visitor import PrimitiveVisitor


@dataclass
class Point:
    x: int = 0

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_point(self)

    def __isub__(self, other):
        x = self.x - other.x

        self.x = x
        return self

    def __add__(self, other):
        vector = deepcopy(self)
        vector += other
        return vector

    def __iadd__(self, other):
        x = self.x + other.x

        self.x = x
        return self


@dataclass
class Vector2:
    x: int = 0
    y: int = 0

    def accept(self, visitor: PrimitiveVisitor):
        return visitor.visit_vector2(self)

    def to_1d(self):
        return Point(self.x)

    def __sub__(self, other):
        vector = deepcopy(self)
        vector -= other
        return vector

    def __isub__(self, other):
        x = self.x - other.x
        y = self.y - other.y

        self.x, self.y = x, y
        return self

    def __add__(self, other):
        vector = deepcopy(self)
        vector += other
        return vector

    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        self.x, self.y = x, y
        return self


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
        vector = deepcopy(self)
        vector -= other
        return vector

    def __isub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        self.x, self.y, self.z = x, y, z
        return self

    def __add__(self, other):
        vector = deepcopy(self)
        vector += other
        return vector

    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        self.x, self.y, self.z = x, y, z
        return self

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

    def __sub__(self, other):
        vector = deepcopy(self)
        vector -= other
        return vector

    def __isub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w

        self.x, self.y, self.z, self.w = x, y, z, w
        return self

    def __add__(self, other):
        vector = deepcopy(self)
        vector += other
        return vector

    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w

        self.x, self.y, self.z, self.w = x, y, z, w
        return self
