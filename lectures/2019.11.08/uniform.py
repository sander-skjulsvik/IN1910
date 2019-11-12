'''
From teacher
'''
import numpy as np
import matplotlib.pyplot as plt


def transition_matrix(states=101):
    M = np.zeros((states, states))

    for i in range(1, states - 1):
        M[i - 1, i] = 0.5
        M[i + 1, i] = 0.5

    M[1, 0] = 0.5
    M[0, 0] = 0.5

    M[states - 2, states - 1] = 0.5
    M[states - 1, states - 1] = 0.5
    assert np.all(np.isclose(np.sum(M, axis=0), 1))
    return M


def probability_vector(N=100, states=101):

    M = transition_matrix(states)
    fig, ax = plt.subplots()
    ax.matshow(M)

    p = np.zeros((states, N + 1))
    starting_position = (states - 1) // 2
    p[starting_position, 0] = 1.0

    for k in range(N):
        p[:, k + 1] = M @ p[:, k]

    fig, ax = plt.subplots(figsize=(12, 4))
    q = ax.matshow(p)
    ax.set_xlabel("Step")
    ax.set_ylabel("x-values")
    ax.set_yticks(np.arange(0, states, 20))
    ax.set_yticklabels(np.arange(-starting_position, starting_position + 1, 20))
    cbar = fig.colorbar(q)
    cbar.set_label("Probability")

    fig, ax = plt.subplots()
    ax.step(range(states), p[:, -1], where="mid")
    ax.set_title("Equilibrium solution")
    ax.set_xlabel("State")
    ax.set_ylabel("Probabilty")
    plt.show()


if __name__ == "__main__":

    probability_vector(states=20)
