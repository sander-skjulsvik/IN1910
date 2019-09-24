import numpy as np


class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2

    def __call__(self, x):
        return self.c0 + self.c1 * x + self.c2 * x ** 2

    def table(self, L, R, n=10):
        """Return a table with n points for L <= x <= R.    
        """
        s = ""
        for x in np.linspace(L, R, n):
            y = self(x)
            s += f"({x:.2f}, {y:.2f})\n"
        return s


class Line1(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)

    def table(self, L, R, n=10):
        s = "This is Line 1\n"
        s += Parabola.table(self, L, R, n)
        return s


class Line2(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)

    def table(self, L, R, n=10):
        s = "This is Line 2\n"
        s += super().table(L, R, n)
        return s


if __name__ == "__main__":

    # Parabola
    p = Parabola(1, 2, 3)
    print(p.table(0, 1))

    # Line
    l = Line1(1, 2)
    print(l.table(0, 1))

    # Line
    l = Line2(1, 2)
    print(l.table(0, 1))
