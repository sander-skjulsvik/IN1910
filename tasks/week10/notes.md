# Task week 10 - Random walks and Marcov Processes

## Task 1: Root Mean Square Displacement of a random Walker
    Average dispplacement of a balanced random walker is
        <X_n> = 0
    in both 1D and 2D. This is bec because the walker has equal changes to go in either direction.
    However, the averaged root mean square displacement, is not 0, it is
        sqrt(<X_n^2>) = sqrt(n), 1-d.

### a: Performing random walks
    Use np.random.randint and np.cumsum to perform 1000 random walks of 500 steps each.

    walker_1D:
        one walker, walkes N step, starts at X0

    walkers_1D_vectorized: 
        M walkers, walk N steps, Starts at X0, if plot_path plots the walker
            