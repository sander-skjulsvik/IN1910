# Markow chains

## Ex: 2 vaser
    To urner, totalt m baller.
    I hver iterasjon flytter vi en tilfedig ball fra den urnen den ligger i til den andre.

    La oss se på en av urnene. Denne urnen kan ha m+1 tilstander. hvorfor?

    Anta at vår urne har n <= m baller

    Skrive et programm:

### Ehrenfest:
    plot som beskrevet.

## Med matriser og prob vector
    Vi lager en prob vektor
        p1= (0,1,0,..,0)
        p2=(1/10, 0, 19/20,0 ,0, ..., 0).

    Transition matrix M
        Pn+1 = M * Pn

    M_i,j er sannynligheten for å gå fra til.

    M: M+1 x M+1

    M_1,0 = 1, M_0,1 = 1/20, M_2,1 = 19/20
    Generelt:
        M_x+1,x = (m-x)/m, M_x-1,x = x/m

    ```python
    def transition_matrix(m):
        M = np.empty((m+1, m+1))
        for x in range(1,m):
            M[x-1, x] = x/m
            M[x+1, x] = (m-x) /m
        M[1,0] = 1
        M[m-1, m] = 1

        return M
    ```

    Finner likevektspunktet
        ...
    
## ladder - stigespillet.
    ladder1.py uten markow
    ladder2.py: markow


