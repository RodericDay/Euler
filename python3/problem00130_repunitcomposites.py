'''
[See 129]

You are given that for all primes, p > 5, that p − 1 is divisible by A(p).
For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first
five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).
'''

from Euler import prime_sieve
from problem00129_repunitdivisibility import *

primes = set(prime_sieve(10**6))

valid = []
for n in (n for n in itertools.count(2) if n not in primes):
    k = A(n)
    if k > 0 and (n-1)%k==0:
        valid.append(n)
    if len(valid) == 25:
        break

ans = sum(valid)
print(ans)

