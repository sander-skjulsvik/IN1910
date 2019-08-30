class Quadratic:
    def __init__(self, a, b, c):
        self.coefficients = a, b, c

    def __call__(self, x):
        a, b, c = self.coefficients
        return a * x ** 2 + b * x + c

    def __str__(self):
        a, b, c = self.coefficients
        return f"{a}x**2 + {b}x + {c}"


def test1():
    # What is really going on
    f = Quadratic(1, 2, 1)
    print(f.__call__(4))


def test2():

    f = Quadratic(1, 2, 1)
    print(f(4))


def test_callable():
    f = Quadratic(1, 2, 1)
    print(callable(f))
    assert callable(f)


def plot():
    import numpy as np
    import matplotlib.pyplot as plt

    f = Quadratic(1, 2, 1)
    g = Quadratic(-1, 4, 4)
    h = Quadratic(0, -2, 3)

    x = np.linspace(-4, 4, 101)
    plt.plot(x, f(x))
    plt.plot(x, g(x))
    plt.plot(x, h(x))
    plt.show()


if __name__ == "__main__":
    test1()
    test2()
    test_callable()
    plot()
