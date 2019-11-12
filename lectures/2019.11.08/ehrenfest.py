import numpy as np
import matplotlib.pyplot as plt

def transition_matrix(m):
    M = np.zeros((m+1, m+1))
    for x in range(1,m):
        M[x-1, x] = x/(2*m)
        M[x+1, x] = (m-x) /(2*m)
        M[x,x] = 0.5  
    M[1,0] = 0.5
    M[m-1, m] = 0.5 

    return M


def ehrenfest_mc():
    m = 20
    N = 100
    # --
    M = transition_matrix(m)
    p = np.zeros((m+1, N+1))
    # print(M)
    p[0, 0] = 1
    for i in range(N):
        p[:, i+1] = M @ p[:, 1]

    fig, ax = plt.subplots()
    q = ax.matshow(p)
    ax.set_xlabel("Iteration number")
    ax.set_ylabel("State")
    fig.colorbar(q)
    plt.show()



def ehrenfest():
    m = 20
    x0 = 10
    N = 1000
    x = np.zeros(N+1)
    # -
    x[0] = x0

    for i in range(N):
        ball = np.random.randint(1, m+1) # draw a ball number

        if ball <= x[i]:
            x[i+1] = x[i] - 1
        else:
            x[i+1] = x[i] + 1

    fig, ax = plt.subplots()
    ax.step(range(N+1), x)
    ax.set_xlabel("Iteration number")
    ax.set_ylabel("Number of balles in")
    plt.show()


if __name__ == "__main__":
    ehrenfest_mc()