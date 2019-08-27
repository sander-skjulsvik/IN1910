import numpy as np
import matplotlib.pyplot as plt

class Polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __call__(self, x):
        SUM = 0
        for exponent in self.coeffs:
            coeff = self.coeffs[exponent]
            SUM += coeff*x**exponent
        return SUM

    def __str__(self):
        STR = ''
        for exponent in self.coeffs:
            coeff = self.coeffs[exponent]
            STR += f'{coeff}*x**{exponent} + '
        return STR[:-3]


if __name__ == "__main__":
    #Exercise 2a) Defining the Polynomial class
    coeffs = {0: 1, 5:-1, 10:1}
    f = Polynomial(coeffs)

    print(f)

    x = np.linspace(-1, 1, 101)
    plt.plot(x, f(x))
    plt.show()