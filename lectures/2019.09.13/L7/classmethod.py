import numpy as np


class SphereOriginal:
    def __init__(self, radius):
        self.radius = radius

    @property
    def volume(self):
        return 4 * np.pi * self.radius ** 3 / 3


class SphereFromVolume:
    def __init__(self, volume):
        self.radius = (3 * volume / (4 * np.pi)) ** (1 / 3)

    @property
    def volume(self):
        return 4 * np.pi * self.radius ** 3 / 3


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    @property
    def volume(self):
        return 4 * np.pi * self.radius ** 3 / 3

    @classmethod
    def from_volume(cls, volume):
        radius = (3 * volume / (4 * np.pi)) ** (1 / 3)
        return cls(radius)


if __name__ == "__main__":

    volume = 5000
    s = Sphere.from_volume(volume)
    print(s.radius)
    s2 = Sphere(s.radius)
    print(s2.volume)

    assert abs(s2.volume - volume) < 1e-10
