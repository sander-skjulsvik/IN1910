# hvordan generere:
    Vi kan kaste terning.
    1995 - bok med 1 milion tilfeldige tall

# hvordan generere på en data.
    Pseudorandom - vi kan ikke finne faktiske tilfeldige tall.
    Tallene må oppføre seg tilfeldige.
    statistisk tilfeldighet

# Pseudorandom Number Generators - PRNG/pRNG
    generer pRandom tall.
    Men må starte en plass.
    Metoder:
        Middle squared mehtod, Linear Congrugential Generators

# Middle-squared Method
    1. Start med et tall (seed), annta at tallet har 4 siffer.
    2. For å finne neste tall, kvadrer tallet, og plukk ut de minste 4 sifferene av det kvadratet.
    3. Gjenta 1 me det nye tallet.

    Da vil alle input være lik i output.

# Linear Congrugential Generators
    As we mentioned, LCGs are a *family* of generators. They all produce random integers by following the governing  difference equation:
    $$X_{n+1} = aX_n + c \mod m.$$
    From this formula, you can see that there are three steps to producing a new number with a LCG:
    1. Multiply the current number by $a$,  the multiplier
    2. Add the constant $c$, the increment
    3. Take the modulo with $m$, the modulus

    comon variables: 
        m = 2**32
        a = 1664525
        c = 1013904223
    
    max val is m.

## Uniform fordeling 
    fordeling a - b 
        Y = (b-a) * X + a

# Box-Muller algoritme for å finne normalfordelte tall
    In Box-Muller, we use two randomly generated independent points on the range $[0, 1)$: $U_1$ and $U_2$, to produce two randomly generated independent normally distributed points: $Z_1$ and $Z_2$.

    This is done through the formula:
    $$\begin{align}
    Z_1 = \sqrt{-2 \ln U_1}\cos (2\pi U_2), \\
    Z_2 = \sqrt{-2 \ln U_1}\sin (2\pi U_2).
    \end{align}$$

# Periodisitet - må man passe på med "Congrugential"
    hvis X0 = xi så vil rekken starte på nytt.
    max periode er m, men kan være mindre.
    Da avhengig ac a, c.

# vanligvis .py
    bruker vi libs for tilfeldige tall.
    som np.random, eller random.
    for seed: np.random.seed(x)

# cpp
    innebygd rand(), bruker vanligvis LCG
    srand for å sette seed, ikke anbefalt

    engine: is generating numbers.
    then we can use f.eks
    uniform_real_distribution: make the rn to my form
    

    