import numpy as np
import matplotlib.pyplot as plt

class Polynomial(object):
    def __init__(self, coeffs):
        coeffs  = AddableDict(coeffs)
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
        coeffs = self.coeffs + other.coeffs
        return Polynomial(coeffs)

    def derivative(self):
        coeffs = {}
        for exponent in self.coeffs:
            coeffs[exponent-1] = self.coeffs[exponent] * exponent
        return Polynomial(coeffs)

class AddableDict(dict):
    def __init__(self, DICT):
        self.DICT = DICT
    
    def __add__(self, other):
        new_DICT = {}
        #running through self.DICT
        for key in self.DICT:
            #if key is in both DICT add
            if key in other.DICT:
                new_DICT[key] =  self.DICT[key] + other.DICT[key]
            #if key is only in self.DICT, add
            else:
                new_DICT[key] = self.DICT[key]
        #running through other.DICT to catch the rest if the exponents
        for key in other.DICT:
            #if key is only in other.DICT, add
            if key not in self.DICT:
                new_DICT[key] = other.DICT[key]
        return  AddableDict(new_DICT)

    def __str__(self):
        return str(self.DICT)

    def __getitem__(self, key):
        return self.DICT[key]


def test_AddableDict():
    a = AddableDict({0: 2, 1: 3, 2: 4})
    b = AddableDict({0: -1, 1:3, 2: 3, 3: 2})
    c = a + b
    assert c[0] == 1
    assert c[1] == 6
    assert c[2] == 7
    assert c[3] == 2

def test_derivative():
    f = Polynomial({10:1, 6:-3, 2:2, 0:1})
    f_deriv = f.derivative()
    print(f'\n\nf = {f}, type f: {type(f)}, f_deriv = {f_deriv}, type f_deriv: {type(f_deriv)}\n\n')
    assert f_deriv.coeffs == {9:10, 5:-18, 1:4}

if __name__ == "__main__":
    # Exercise 2a) Defining the Polynomial class
    # coeffs = {0: 1, 5:-1, 10:1}
    # f = Polynomial(coeffs)

    # print(f)

    # x = np.linspace(-1, 1, 101)
    # plt.plot(x, f(x))
    # plt.show()

    # Exercise 2b): Adding general polynomials together
    # f = Polynomial({0:1, 5:-7, 10:1})
    # g = Polynomial({5:7, 10:1, 15:-3})

    # print(f+g)

    # # Exercise 2c) Defining a AddableDictionary class
    # a = AddableDict({0: 2, 1: 3, 2: 4})
    # b = AddableDict({0: -1, 1:3, 2: 3, 3: 2})
    # print(a + b)

    # test_AddableDict()

    # Exercise 2d) Derivative of a polynomial
    test_derivative()   


