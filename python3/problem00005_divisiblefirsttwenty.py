'''
What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
'''

import collections
import operator
import functools
from problem00003_primefactor import prime_factors

@functools.lru_cache(maxsize=None)
def factorize(n):

    for f in prime_factors(n):
        if n%f==0:
            return collections.Counter({f:1}) + factorize(n//f)

    return collections.Counter({n:1}) if n>1 else collections.Counter()

def merge(d1, d2, comparef):
    all_keys = set(d1)|set(d2)
    return {key:comparef(d1.get(key, 0), d2.get(key, 0)) for key in all_keys}

def product(iterable):
    return functools.reduce(operator.mul, iterable)


if __name__ == '__main__':
    required = {}
    for n in range(20):
        required = merge(required, factorize(n), max)

    ans = product([k**v for k, v in required.items()])
    print(ans)
