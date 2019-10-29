import time

class NumRecipiesLCG:
    def __init__(self, seed):
        self._state = seed

        self._m = 2**32
        self._a = 1664525
        self._c = 1013904223

    def __call__(self):
        a, c, m, current = self._a, self._c, self._m, self._state
        self._state = (a*current + c) % m
        return self._state
        

if __name__ == "__main__":
    random = NumRecipiesLCG(1234)

    # 0 to 1
    for _ in range(time.time_ns()):
        print(random() /2**32)
        # Y = (b-a) * X + a
        print(Y)