import numpy as np
import matplotlib.pyplot as plt


def transition_matrix(states=101):
    M = np.zeros((states, states))

    for i in range(states - 6):
        M[i + 1 : i + 7, i] = 1 / 6

    # Handle "overshoot"
    for i in range(states - 6, states - 1):
        M[i + 1 : states - 1, i] = 1 / 6
        M[-1, i] = (6 - (states - 2 - i)) / 6
    M[-1, -1] = 1

    assert np.all(np.isclose(np.sum(M, axis=0), 1))
    return M


def probability_vector(N=50, states=101):

    M = transition_matrix(states)
    fig, ax = plt.subplots()
    ax.matshow(M)

    p = np.zeros((states, N + 1))
    p[0, 0] = 1.0

    for k in range(N):
        p[:, k + 1] = M @ p[:, k]

    fig, ax = plt.subplots(figsize=(4, 8))
    q = ax.matshow(p)
    ax.set_xlabel("Rolls")
    ax.set_ylabel("Position")
    cbar = fig.colorbar(q)
    cbar.set_label("Probability")

    fig, ax = plt.subplots()
    ax.step(range(N + 1), p[-1, :])
    ax.set_xlabel("Rolls")
    ax.set_ylabel("Probability of being finished")

    fig, ax = plt.subplots()
    ax.step(range(N + 1), np.gradient(p[-1, :]))
    ax.set_xlabel("Rolls")
    ax.set_ylabel("Probability of arriving at finish")

    plt.show()


if __name__ == "__main__":

    probability_vector(N=50, states=101)
