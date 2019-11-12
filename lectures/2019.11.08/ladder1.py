import numpy as np
import matplotlib.pyplot as plt

def ladder():

    N = 10000
    all_rolls = np.empty(N)

    for i in range(N):
        position = 0
        num_rolls = 0
        while position < 100:
            roll = np.random.randint(1,7)
            position += roll
            num_rolls += 1
        all_rolls[i] = num_rolls

    print(f"Best: {np.min(all_rolls)}")
    print(f"worst: {np.max(all_rolls)} ")
    print(f"Mean: {np.mean(all_rolls)}")
    print(f"Theoretical best: {np.ceil(100 / 6)}")
    print(f"Theoretical mean: {np.ceil(100 / 3.5)}")

    fig, ax = plt.subplots()
    ax.hist(all_rolls, bins=range(50))
    plt.show()

if __name__ == "__main__":
    ladder()