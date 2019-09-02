from Exercise2_A_class_for_general_polynomials import Polynomial as P

class HOWF:
    def __init__(self, n):
        self.H = P({0:1,1:2})
        self.H[n] = self._compute_Hermite(n)

    def __call__(self, x):
        return self.H(x)

    def _compute_Hermite(self, n):
        H = self.H
        print(f'H = {H}, n = {n}')
        return P({1:2})*P(H[n-1]) + P({0:n-1})*P(H[n-2])
    
    


def test_Hermite():
    H0 = lambda x: 1
    H1 = lambda x: 2*x
    H2 = lambda x: 4*x*x - 2
    H3 = lambda x: 8*x**3 - 12*x
    H4 = lambda x: 16*x**4 - 48*x**2 + 12
    H5 = lambda x: 32*x**5 - 160*x**3 + 120*x
    H_table = [H0, H1, H2, H3, H4, H5]
    
    tol = 1e-12
    for n in range(2, 6):
        H = HOWF(n).H
        for x in [0, 0.5, 1.0/3, 1, 3/2, 2]:
            expected = H_table[n](x)
            computed = H(x)
            msg = "The implemented Hermite Polynomial yields unexpected result for n = %d\
            \n\tH(%.2f) = %.13g != %.13g" %(n, x, expected, computed)
            assert abs(expected - computed) < tol, msg


if __name__ == "__main__":
    test_Hermite()