# Mixed programming with C, C++ and py
Bruker det faktum at python er skrevet i C

## før man optimaliserer, sjekk om man bruker den riktige algoritmen.
sorting: quick sort, boubble sort

    Bouble:
        O(n^2)
    Quick:
        O(n*log(n))

```python
import sys; sys.path.insert(0, "code")
import numpy as np
from bubblesort import bubblesort
from quicksort import quicksort
numbers = np.random.randint(100, size=100)

s = sorted(numbers)
b = bubblesort(numbers)
q = quicksort(numbers)


assert np.all(s == b)
assert np.all(s == q)
assert np.all(b == q)
```
Sorted i pyhton: return list
    Bruker algoritmen: Timsort


