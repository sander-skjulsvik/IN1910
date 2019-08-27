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

    def __add__(self, other):
        coeffs = self.coeffs
        new_coeffs = {}
        #running through self.coeffs
        for exponent in self.coeffs:
            #if exponent is in both coeffs add
            if exponent in other.coeffs:
                new_coeffs[exponent] =  self.coeffs[exponent] + other.coeffs[exponent]
            #if exponent is only in self.coeffs, add
            else:
                new_coeffs[exponent] = self.coeffs[exponent]
        #running through other.coeffs to catch the rest if the exponents
        for exponent in other.coeffs:
            #if exponent is only in other.coeffs, add
            if exponent not in self.coeffs:
                new_coeffs[exponent] = other.coeffs[exponent]
        return Polynomial(new_coeffs)




if __name__ == "__main__":
    # Exercise 2a) Defining the Polynomial class
    # coeffs = {0: 1, 5:-1, 10:1}
    # f = Polynomial(coeffs)

    # print(f)

    # x = np.linspace(-1, 1, 101)
    # plt.plot(x, f(x))
    # plt.show()

    # Exercise 2b): Adding general polynomials together
    f = Polynomial({0:1, 5:-7, 10:1})
    g = Polynomial({5:7, 10:1, 15:-3})
    
    print(f+g)
