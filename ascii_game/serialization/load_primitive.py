from ascii_game.primitive.color_a import ColorA
from ascii_game.primitive.vector import Vector3
from ascii_game.render.texture import ObjectTexture


def load_vector3(vector: dict) -> Vector3:
    return Vector3(vector["x"], vector["y"], vector["z"])


def load_color_a(color: dict) -> ColorA:
    return ColorA(color["r"], color["g"], color["b"], color["a"])


def load_object_texture(object_id: str) -> ObjectTexture:
    return ObjectTexture(object_id)
