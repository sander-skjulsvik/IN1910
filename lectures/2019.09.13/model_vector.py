import numpy as np


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3D(x, y, z)


class ModelVectorInherit(Vector3D):
    def __init__(self, name, x, y, z):
        self.name = name
        super().__init__(x, y, z)

    def __add__(self, other):
        vector_sum = super().__add__(other)
        return ModelVectorInherit(
            "+".join([self.name, other.name]), vector_sum.x, vector_sum.y, vector_sum.z
        )


class ModelVectorComposition:
    '''
    Arguments
    ------------------
    name: str
        Name of the model vector
    vector: Vector3d
        The vector
    '''
    def __init__(self, name, vector):
        self.name = name
        self.vector = vector

    def __add__(self, other):
        return ModelVectorComposition(
            name="+".join([self.name, other.name]), vector=self.vector + other.vector
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.vector})"


def test_model_vector_inherit():
    u = ModelVectorInherit("vector1", 2, 0, -2)
    v = ModelVectorInherit("vector2", 2, 4, 2)
    w = u + v

    print(f"{u} + {v} = {w}")
    print(w.name)


def test_model_vector_composition():
    u = ModelVectorComposition("vector1", Vector3D(2, 0, -2))
    v = ModelVectorComposition("vector2", Vector3D(2, 4, 2))
    w = u + v

    print(f"\n{u} + {v} = {w}")
    print(w.name)


def test_model_vector_composition_for_free():
    u = ModelVectorComposition("first value", 2)
    v = ModelVectorComposition("second value", 4)
    w = u + v

    print(f"\n{u} + {v} = {w}")
    print(w.name)


if __name__ == "__main__":
    test_model_vector_inherit()
    test_model_vector_composition()
    test_model_vector_composition_for_free()
