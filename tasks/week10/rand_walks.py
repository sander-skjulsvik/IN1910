import numpy as np
import matplotlib.pyplot as plt

def walker_1D(N = 20, X0 = 0, show=True):
    X = np.empty(N+1)
    X[0] = X0
    for i in range(N):
        X[i+1] = X[i] + 2*np.random.randint(2) -1
    if show:
        plot(X)

def walkers_1D_vectorized(N = 20, M = 2, X0 = 0, plot_path=True):
    X = np.empty((N, M)) 
    X[0] = X0 # init val
    K = 2*np.random.randint(2, size=(N-1, M)) - 1 # step
    X[1:, :] = X[0, :] + np.cumsum(K, axis=0) # vectorized sum

    if plot_path is True:
        plot(X)

def plot(X, s = None):
    y = X
    x = range(len(y))
    fig, ax = plt.subplots()
    if  M <= 10:
        alfa = 1
    else:
        alfa= 10/M
    ax.step(x,y, where="mid", alpha=alfa, color="g")
    ax.set_xlabel(" Nr of steps taken")
    ax.set_ylabel(" Displacement ")
    plt.show()



if __name__ == "__main__":
    num_walkers = M = 1000
    num_steps = N = 500
    # walker_1D(num_steps)
    walkers_1D_vectorized(N, M)


