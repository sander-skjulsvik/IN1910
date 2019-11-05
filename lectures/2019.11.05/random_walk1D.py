import numpy as np
import matplotlib.pyplot as plt
import time

def random_walk_vectorized(N = 1000, x0=0,M=1, plot_trace=True):
    # vectorized
    X = np.empty((N+1, M))
    X[0, :] = x0
    K = 2*np.random.randint(2, size=(N, M))-1 # -1,1
    # from IPython import embed; embed()
    X[1:, :] = X[0, :] + np.cumsum(K, axis=0)
    
    if plot_trace:
        plot(X)


def random_walk_py(N = 100_000, plot_trace=True):
    # py implementation
    x0 = 0
    X = np.empty(N+1)
    X[0] = x0
    for i in range(N):
        # K = 2*np.random.randint(2)-1
        K = np.random.choice([-1,1])
        X[i+1] = X[i] + K
    
    if plot_trace:
        plot(X)


def plot(X):
    fig, ax = plt.subplots()
    N = len(X)
    ax.plot(range(N+1), X, alda=0.01, color="k")
    # ax.step(range(N+1), X)

    ax.set_xlabel("Iteration")
    ax.set_ylabel("Position")
    plt.show()

def test_performance():
    '''
    Not done!
    '''
    N = 100_000
    # t0 = time.
    random_walk_py(N=N)
    random_walk_vectorized(N=N)

def test_many_objects():
    random_walk_vectorized(N=100_000, x0=0, M=10, plot_trace=True)
if __name__ == "__main__":

    test_many_objects()
