'''
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
1219 is the smallest number such that the last digits are formed by p1 whilst
also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive
primes, p2 > p1, there exist values of n for which the last digits are formed
by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
'''

from Euler import prime_sieve
import math

def S(p1, p2):
    # m * p2 = k * 10 ** e + p1
    # p1 and p2 are coprime so CRT

    # d = 10 ** e
    d = 10 ** math.ceil(math.log10(p1))

    # k * d + p1 == 0 (mod p2)
    # k == (p2 - p1) * d_inv (mod p2)
    # but precisely because p2 is prime we can take shortcut
    # and avoid doing modular inverse the long way
    d_inv = pow(d, p2-2, p2)
    k = (p2 - p1) * d_inv % p2

    return k * d + p1

primes = list(prime_sieve(1000000+100))
ans = sum(S(p1, p2) for p1, p2 in zip(primes, primes[1:]) if 5 <= p1 <= 1000000)
print(ans)
