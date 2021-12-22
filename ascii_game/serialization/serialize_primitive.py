from ascii_game.primitive.color_a import ColorA
from ascii_game.primitive.vector import Vector3, Point, Vector2, Vector4


def serialize_point(element: Point):
    return {"x": element.x}


def serialize_vector2(element: Vector2):
    return {"x": element.x, "y": element.y}


def serialize_vector3(element: Vector3):
    return {"x": element.x, "y": element.y, "z": element.z}


def serialize_vector4(element: Vector4):
    return {"x": element.x, "y": element.y, "z": element.z, "w": element.w}


def serialize_color_a(element: ColorA):
    return {"r": element.r, "g": element.g, "b": element.b, "a": element.a}
