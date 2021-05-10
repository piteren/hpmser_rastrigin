import random
from typing import List

from ptools.lipytools.decorators import timing

@timing
def generate(n,m) -> List[List[float]]:
    return [[random.random() for _ in range(n)] for _ in range(m)]

@timing
def sort(nm: List[List[float]]):
    for l in nm:
        l.sort()

@timing
def top_k(nm: List[List[float]], k: int):
    for l in nm:
        for _ in range(k):
            e = max(l)
            l.remove(e)

n = 10000

nm = generate(n,n)
sort(nm)

nm = generate(n,n)
top_k(nm,5)
