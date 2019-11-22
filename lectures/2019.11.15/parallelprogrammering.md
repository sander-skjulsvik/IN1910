# paralellprogrammering.

## Super pc
    UiO - Abel
    NTNU - Saga
    UiT - ...

Super computers kraft er målt i FLOPS

## I/O bound
* problemer der vi må vente
* laste ned data fra nettet
* Lese/ Skrive til disk
* Multithreding

## CPU bound
* Problemer der vi har mye som må gjøres.
* Multiprosessing

## Multithreding
* En magnus
* Os som bestemmer når man bytter jobb.
* finnes et alternativ: async

## Multiprocessing
* Vi lager N kopier som gjør samme jobben.
* Oppgavene må være uavhengige.


## IN3200 Vidre med multicore prossessing.


## map
* map er en funksjon som helt sentral i de fleste funksjonell programeringspråk
* map tar en funskjon og en liste med elementer med funksjonen anvendt på hvert element.

```python
def func(n):
    return sum(range(n))

x = [1,2,3,4]
y = [func(xi) for xi in x]
z = map(func, x)

print("y: ", y )
print("z: ", z )
print("list(z): ", list(z) )

```
## paralell i python
* concurrent.futures
* Vi må bruke context manager, og en executer
```python
import concurrent.futures
t0 = time.perf_counter()
...
```
ProcessPoolExecutor:
    multiprocess

