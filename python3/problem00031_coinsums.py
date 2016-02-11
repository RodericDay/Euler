'''
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def k(y, xs):
    if y < 0:
        return 0

    if y==0:
        return 1

    return sum(k(y-x, xs[i:]) for i, x in enumerate(xs))

def knapsack(target, options):
    options = tuple(sorted(options, reverse=True))
    return k(target, options)

options = (1, 2, 5, 10, 20, 50, 100, 200)
ans = knapsack(200, options)
print(ans)
