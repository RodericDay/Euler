'''
What is the value of the first triangle number
to have over five hundred divisors?
'''

import itertools
from problem00005_divisiblefirsttwenty import factorize, product

def number_of_divisors(n):
    factors = factorize(n) # { factor : multiplicity }
    if factors:
        return product(m+1 for m in factors.values())
    return 0

def triangle_numbers():
    total = 0
    for n in itertools.count(1):
        total += n
        yield total


if __name__ == '__main__':
    ans = next(n for n in triangle_numbers() if number_of_divisors(n) > 500)
    print(ans)
