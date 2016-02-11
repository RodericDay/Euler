'''
Define f(0)=1 and f(n) to be the number of different ways n can be expressed
as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10^25)?
'''

from math import log, ceil
from functools import lru_cache

def lim(n):
    return ceil(log(n)/log(2))

def generate_options(n):
    return [2**e for e in range(lim(n)) for _ in range(2)]

def unique_enumerate(xs):
    seen = set()
    for i, x in enumerate(xs):
        if x not in seen:
            yield (i, x)
            seen.add(x)

@lru_cache(maxsize=None)
def knapsack(n, options):
    '''
    since the knapsack doesn't allow items to be replenished, drawing instead
    from a collection, three optimizations are available:
    - sum(options) < n
    - unique_enumerate
    - options[i+1:]
    '''
    if n < 0 or sum(options) < n:
        return 0

    if n == 0:
        return 1

    return sum(knapsack(n-x, options[i+1:]) for i, x in unique_enumerate(options))

n = 10**25
options = tuple(reversed(generate_options(n)))
ans = knapsack(n, options)
print(ans)
