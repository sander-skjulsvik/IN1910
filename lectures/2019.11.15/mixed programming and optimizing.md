# mixed programming and optimizing

## mixed
Skriver koden som man skriver med i python. Mens de tunge beregningene skrives i C.
Vanlig hvis man har mye for løkker.
C: ctype

## cyton:
C + pyhon
skriver kode som ligner på python, men det kompileres til C
for å skrive cton set .pyx
import pyximport.install(); import ctriangle for å importere .pyx
%% cton -a
    for å vise hvor cyton bruker python.

cimport numpy as np
    np.ndarray(double, ndim=2)
cpyton kan skru av error som indexerror, dette kan øke ytelsen. Dette kan funke på forksjellige ting
    #cython: boundscheck=False
    #cython: wraparound=False
### hjelpe cyton
```python

%% cyton # i notebook.
    def triangle(n):
        cdef int i
        cdef int total = 0
        tot = 0
        for i in range(1, n+1):
            tot += 1
        return tot
```

### triangle(n):
```python
%% cyton # i notebook.
    def triangle(n):
        tot = 0
        for i in range(1, n+1):
            tot += 1
        return tot
```


## test problem diffusjonsligningen
bruker profiler for å finne ut hvor treg programet er.
1. vectoriserer.
    raskere siden mye av numy er i C

## numba
@numba.jit (just in time)
over en vectorisert
fortelle numba at vi vill at alt skal være c
    @numba.jit(nopython=True)
## andre værktøy
    PyPy - python med jit-kompilering
    Swig - Kan brukes til å wrappe kode ksrevet i et annet språk
    Ctyps /cffi - calle c funcs fra py
    Pybind11 
    Instant / Dijitso

## time programmet
    %timeit -o -y function
    profiler
