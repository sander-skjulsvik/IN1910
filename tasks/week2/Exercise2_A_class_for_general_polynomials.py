import numpy as np
import matplotlib.pyplot as plt



class AddableDict(dict):
    # def __init__(self, DICT):
    #     super().__init__(DICT)
    
    def __add__(self, other):
        _new = {}
        #running through self.DICT
        for key in self:
            #if key is in both DICT add
            if key in other:
                _new[key] =  self[key] + other[key]
            #if key is only in self.DICT, add
            else:
                _new[key] = self[key]
        #running through other.DICT to catch the rest if the exponents
        for key in other:
            #if key is only in other.DICT, add
            if key not in self:
                _new[key] = other[key]
        new = AddableDict(_new)
        #print(f'AddableDict.__add__: self={self}, other={other}, new={new}')
        return  new


class Polynomial(AddableDict):
    # def __init__(self, coeffs):
    #     coeffs  = AddableDict(coeffs)
    #     self = coeffs
    def __init__(self, DICT):
        super().__init__(DICT)
        self.coeffs = DICT

    def __call__(self, x):
        SUM = 0
        for exponent in self:
            coeff = self[exponent]
            SUM += coeff*x**exponent
        return SUM

    def __str__(self):
        STR = ''
        for exponent in self:
            coeff = self[exponent]
            STR += f'{coeff}*x**{exponent} + '
        #print(f'Polynomial.__str__: STR={STR}')
        return STR[:-3]
    
    def __mul__(self, other):
        _new = {}
        for i in self:
            for j in other:
                _new[i+j] = self[i]*other[j]
        return Polynomial(_new)
                

    def derivative(self):
        coeffs = {}
        if 0 in self:
            del self[0]
        for exponent in self:
            coeffs[exponent-1] = self[exponent] * exponent
        return Polynomial(coeffs)


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
    # print(f'\n\nf = {f}, type f: {type(f)}, f_deriv = {f_deriv}, type f_deriv: {type(f_deriv)}\n\n')
    assert f_deriv.coeffs == {9:10, 5:-18, 1:4}

def test_Polynomial_mul():
    f = Polynomial({2: 4, 1: 1})
    g = Polynomial({3: 3, 0: 1})
    h = f*g
    assert h.coeffs == {5:12, 4:3, 2:4, 1:1}

if __name__ == "__main__":
    # Exercise 2a) Defining the Polynomial class
    # coeffs = {0: 1, 5:-1, 10:1}
    # f = Polynomial(coeffs)

    # print(f)

    # x = np.linspace(-1, 1, 101)
    # plt.plot(x, f(x))
    # plt.show()

    # Exercise 2b): Adding general polynomials together
    # print('hello world')
    # f = Polynomial({0:1, 5:-7, 10:1})
    # g = Polynomial({5:7, 10:1, 15:-3})

    # print(f'f+g = {str(f+g)}')

    # # Exercise 2c) Defining a AddableDictionary class
    # a = AddableDict({0: 2, 1: 3, 2: 4})
    # b = AddableDict({0: -1, 1:3, 2: 3, 3: 2})
    # print(a + b)

    # test_AddableDict()

    # Exercise 2d) Derivative of a polynomial
    # test_derivative()  

    # Exercise 2e) Multiplying polynomials
    #try
    f = Polynomial({2: 4, 1: 1})
    g = Polynomial({3: 3, 0: 1})
    print(f*g)
    #test
    test_Polynomial_mul()

