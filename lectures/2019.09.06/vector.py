import numpy as np


class Vector:
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y

        if z is None:
            self.dim = 2
            z = 0
        else:
            self.dim = 3

        self.z = z

    def __str__(self):
        if self.dim == 2:
            return f"({self.x:g}, {self.y:g})"
        else:
            return f"({self.x:g}, {self.y:g}, {self.z:g})"

    def __repr__(self):
        if self.dim == 2:
            return f"{self.__class__.__name__}({self.x}, {self.y})"
        else:
            return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        msg = f"Cannot add Vector with {type(other)}"
        # assert isinstance(other, Vector), msg
        if not isinstance(other, Vector):
            raise TypeError(msg)
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vector(x, y, z)

    def __eq__(self, other):
        msg = f"Cannot compare Vector with {type(other)}"
        if not isinstance(other, Vector):
            raise TypeError(msg)

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __sub__(self, other):
        msg = f"Cannot subtract Vector with {type(other)}"
        # assert isinstance(other, Vector), msg
        if not isinstance(other, Vector):
            raise TypeError(msg)
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vector(x, y, z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def __mul__(self, other):
        """Interpret u*v to be the dot product"""
        if isinstance(other, Vector):
            return self.dot(other)
        elif isinstance(other, (int, float)):
            # Alternative use `np.isscalar`
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError(f"cannot multiply vector and {type(other)}")

    def __matmul__(self, other):
        """Interpret u@v as cross product"""
        return self.cross(other)

    def perpendicular(self, other):
        return abs(self * other) < 1e-9

    def __rmul__(self, other):
        return self * other

    @property
    def length(self):
        return np.sqrt(self * self)

    @length.setter
    def length(self, new_length):
        scale = new_length / self.length
        self.x *= scale
        self.y *= scale
        self.z *= scale

    def unit(self):
        new_vector = Vector(self.x, self.y, self.z)
        new_vector.length = 1
        return new_vector

    def __len__(self):
        return self.dim
