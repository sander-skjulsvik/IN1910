import numpy as np
import matplotlib.pyplot as plt
import time

def random_walk(N = 1000, x0=0,plot_trace=True):
    # vectorized
    R = np.empty((N+1, N+1))
    possible_choices = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    R[0, :] = x0

    for i in range(N):
        K = possible_choices[np.random.randint(4)] # random choice

        R[i+1, :] =  R[i, :] + K

    if plot_trace:
        plot(R)

def plot(R):
    
    fig, ax = plt.subplots()
    ax.plot(R[:, 0], R[:, 1])
    plt.show()


if __name__ == "__main__":
    random_walk()
