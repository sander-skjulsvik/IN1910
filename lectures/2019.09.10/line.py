import numpy as np

class Parabola:
    def __init__(self, c0,c1,c2):
        self.c0, self.c1, self.c2 = c0, c1, c2

    def __call__(self, x):
        return self.c0 + self.c1*x + self.c2*x**2

    def table(self, L, R, N):

        t = np.linspace(L, R, N)
        s = f'{self.__class__.__name__} \n'
        for x in t:
            s += f"{x:.2f}, {self(x):.2f} \n"
        return s

class Line(Parabola):
    # name = 'Line'
    def __init__(self, c0, c1):
        # Parabola.__init__(self, c0, c1, c2)
        super().__init__(c0, c1, 0)
    
    def table(self, L, R, n):
        s = super().table(L, R, n)
        return s
   

if __name__ == "__main__":
    p = Parabola(1,2,3)
    s = p.table(0,1,10)
    print(s)
    # print(p(2))

    l = Line(1,2)
    s = l.table(0,1,10)
    print(s)
    # print(l(2))