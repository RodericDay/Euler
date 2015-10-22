'''
What is the largest prime factor of the number 600851475143?
'''

import itertools

def prime_sieve(n):
    sieve = [True] * int(n+1) # this is not identical to a list comprehension!
    sieve[0] = sieve[1] = False
    for p in (p for p, is_prime in enumerate(sieve) if is_prime):
        if p**2 < n: sieve[2*p::p] = [False] * int(n/p-1)
        yield p

def prime_factors(n):
    lim = n**0.5+1
    below_lim = lambda x: x < lim
    primes = prime_sieve(lim)
    return (p for p in itertools.takewhile(below_lim, primes) if n%p==0)


if __name__ == '__main__':
    ans = max(prime_factors(600851475143))
    print(ans)
