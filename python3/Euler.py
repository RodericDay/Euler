import itertools
import functools
import operator
import collections

def subsequences(iterable, length):
    yield from zip(*[iterable[start:] for start in range(length)])

def product(iterable):
    return functools.reduce(operator.mul, iterable)

def prime_sieve(n):
    sieve = [True] * int(n+1) # this is not identical to a list comprehension!
    sieve[0] = sieve[1] = False
    for p in (p for p, is_prime in enumerate(sieve) if is_prime):
        if p**2 < n: sieve[2*p::p] = [False] * int(n/p-1)
        yield p
