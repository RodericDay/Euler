'''
What is the largest prime factor of the number 600851475143?
'''

from Euler import prime_sieve
import itertools

def prime_factors(n):
    lim = n**0.5+1
    below_lim = lambda x: x < lim
    primes = prime_sieve(lim)
    return (p for p in itertools.takewhile(below_lim, primes) if n%p==0)


if __name__ == '__main__':
    ans = max(prime_factors(600851475143))
    print(ans)
