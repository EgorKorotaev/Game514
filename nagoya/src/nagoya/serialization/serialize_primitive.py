from nagoya.primitive import ColorA, Vector2, Vector3


def serialize_vector2(element: Vector2):
    return {"x": element.x, "y": element.y}


def serialize_vector3(element: Vector3):
    return {"x": element.x, "y": element.y, "z": element.z}


def serialize_color_a(element: ColorA):
    return {"r": element.r, "g": element.g, "b": element.b, "a": element.a}
