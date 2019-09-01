import sys
from math import pi,sqrt


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        assert radius >= 0, 'must be positive'
        self._radius = radius

    @property
    def area(self):
        return 4 * pi * self.radius ** 2

    @area.setter
    def area(self, area):
        self.radius = 1/4 * sqrt(area)

    @property
    def volume(self):
        return 4 * pi * self.radius ** 3 / 3

    @volume.setter
    def volume(self, volume):
        self.radius = 3/4 * volume ** (1/3)


football = Sphere(11)
# print(football.area())
print(f'football.radius:{football.radius},football.area:{football.area}, football.volume:{ football.volume}')
football.radius = 8
# print(football.area())
print(f'football.radius:{football.radius},football.area:{football.area}, football.volume:{ football.volume}')
football.volume = 10
print(f'football.radius:{football.radius},football.area:{football.area}, football.volume:{ football.volume}')
football.radius = -1