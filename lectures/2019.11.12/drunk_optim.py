import numpy as np
import matplotlib.pyplot as plt


class DrunkardsWalk:
    def __init__(self, home, N=100):
        self.x = 0
        self.home = home
        self.history = [0]
        self._N = N
        self.make_steps()

    @property
    def position(self):
        return self.x

    def make_steps(self):
        self._steps = 2 * np.random.randint(2, size=self._N) - 1
        self._i = 0

    @property
    def steps(self):
        return len(self.history)

    def is_at_home(self):
        return self.position == self.home

    def step(self):
        if self._i >= self._N:
            self.make_steps()

        self.x += self._steps[self._i]
        self._i += 1
        self.history.append(self.x)

    def walk_home(self):
        while not self.is_at_home():
            self.step()
        return self.steps

    def plot(self):
        plt.plot(range(self.steps), self.history, alpha=0.7)


def single():
    drunkard = DrunkardsWalk(100)
    steps = drunkard.walk_home()
    # drunkard.plot()

    print(drunkard.steps)


def multiple():
    for walker in range(5):
        drunkard = DrunkardsWalk(100)
        drunkard.walk_home()
        drunkard.plot()


if __name__ == "__main__":
    np.random.seed(100122)
    single()
    # multiple()
    # plt.show()
    plt.close()
