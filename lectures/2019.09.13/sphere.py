from math import pi, sqrt

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    @property
    def volume(self):
        return (4*pi/3) * self.radius**3

    @classmethod
    def from_volume(cls, volume):
        radius = ((volume/pi)*(3/4))**(1/3)

        return cls(radius)


class SphereFromVolume:
    def __init__(self, volume):
        self.radius = ((volume/pi)*(3/4))**(1/3)

    @property
    def volume(self):
        return (4*pi/3) * self.radius**3

if __name__ == "__main__":
    s1 = Sphere(10)
    print(s1.volume)

    s2 = Sphere.from_volume(4188.790204786391)
    print(s2.volume)
    print(s2.radius)