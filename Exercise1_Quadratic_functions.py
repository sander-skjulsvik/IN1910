import matplotlib.pyplot as plt
import numpy as np

class Quadratic(object):
    def __init__(self, a_2, a_1, a_0):
        self.a2, self.a1, self.a0 = a_2,a_1,a_0

    def __call__(self, x):
        return self.a2*x**2 + self.a1*x + self.a0

    def __str__(self):
        return (f'{self.a2}*x**2 + {self.a1}*x + {self.a0}')

    def __add__(self, other):
        b0 = self.a0 + other.a0
        b1 = self.a1 + other.a1
        b2 = self.a2 + other.a2
        return Quadratic(b2,b1,b0)
    
    def __sub__(self, other):
        b0 = self.a0 - other.a0
        b1 = self.a1 - other.a1
        b2 = self.a2 - other.a2
        return Quadratic(b2,b1,b0)

    
    def roots(self):
        a, b, c = self.a2, self.a1, self.a0
        #two results
        if b**2 - 4*a*c > 0:
            x1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
            x0 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
            x = (x0,x1)
        #two complex results
        elif b**2 - 4*a*c < 0:
            #Ignore imaginary ones
            x = ()
        #one result
        else:
            x0 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
            x = (x0,x0)
        return x

    def intersect(self, other):
        h = self - other
        roots = h.roots()
        intersection_points = []
        for root in roots:
            intersection_points.append( (root,self(root)) )
        return intersection_points




def test_Quadratic():
        f = Quadratic(1, -2, 1)
        assert abs(f(-1) - 4) < 1e-8
        assert abs(f(0)  - 1) < 1e-8
        assert abs(f(1)  - 0) < 1e-8

def test_Quadratic_add():
    f = Quadratic(1, -2, 1)
    g = Quadratic(-1, 6, -3)
    h = f + g
    a2, a1, a0 = h.a2, h.a1, h.a0
    assert a2 == 0
    assert a1 == 4
    assert a0 == -2

def test_Quadratic_root():
    f1 = Quadratic(2, -2, 2)
    f2 = Quadratic(1, -2, 1)
    f3 = Quadratic(1, -3, 2)
    
    assert f1.roots() == ()
    assert abs(f2.roots()[0] - 1) < 1e-8
    assert abs(f3.roots()[0] - 1) < 1e-8 and abs(f3.roots()[1] - 2) < 1e-8
    

if __name__ == "__main__":
    # #test
    # f = Quadratic(1, -2, 1)
    # x = np.linspace(-5, 5, 101)
    # plt.plot(x, f(x))
    # plt.show()

    # test_Quadratic()


    # #try Quadratic str
    # print(f)
    

    #try __add__
    # f = Quadratic(1, -2, 1)
    # g = Quadratic(-1, 6, -3)

    # h = f + g
    # print(h)

    # x = np.linspace(-5, 5, 101)
    # plt.plot(x, h(x))
    # plt.show()

    # test_Quadratic_add()

    #Root
    # test_Quadratic_root()

    # Intersection
    f = Quadratic(1, -2, 1)
    g = Quadratic(2, 3, -2)
    f_g_intersect_points = f.intersect(g)

    x = np.linspace(-6,6,1000)
    plt.plot(x,f(x), x,g(x))
    for point in f_g_intersect_points:
        plt.plot(point[0], point[1], "*")
    plt.show()