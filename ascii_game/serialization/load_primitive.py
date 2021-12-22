from ascii_game.primitive.vector import Vector3


def load_vector3(vector: dict) -> Vector3:
    return Vector3(vector["x"], vector["y"], vector["z"])
