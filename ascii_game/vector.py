class Vector1:
    def __init__(self, x: float = 0.0):
        self.x = x

    def get_float_x(self):
        return self.x

    def get_int_x(self):
        return int(self.x)


class Vector2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def get_float_x(self):
        return self.x

    def get_int_x(self):
        return int(self.x)

    def get_float_y(self):
        return self.y

    def get_int_y(self):
        return int(self.y)


class Vector3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_float_x(self):
        return self.x

    def get_int_x(self):
        return int(self.x)

    def get_float_y(self):
        return self.y

    def get_int_y(self):
        return int(self.y)

    def get_float_z(self):
        return self.z

    def get_int_z(self):
        return int(self.z)


class Vector4:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def get_float_x(self):
        return self.x

    def get_int_x(self):
        return int(self.x)

    def get_float_y(self):
        return self.y

    def get_int_y(self):
        return int(self.y)

    def get_float_z(self):
        return self.z

    def get_int_z(self):
        return int(self.z)

    def get_float_w(self):
        return self.w

    def get_int_w(self):
        return int(self.w)
