import matplotlib.pyplot as plt
import numpy as np

class Quadratic(object):
    def __init__(self, a_2, a_1, a_0):
        self.a2, self.a1, self.a0 = a_2,a_1,a_0

    def __call__(self, x):
        return self.a2*x**2 + self.a1*x + self.a0


def test_Quadratic():
        f = Quadratic(1, -2, 1)
        assert abs(f(-1) - 4) < 1e-8
        assert abs(f(0)  - 1) < 1e-8
        assert abs(f(1)  - 0) < 1e-8

if __name__ == "__main__":
    #test
    f = Quadratic(1, -2, 1)
    x = np.linspace(-5, 5, 101)
    plt.plot(x, f(x))
    plt.show()

    test_Quadratic()