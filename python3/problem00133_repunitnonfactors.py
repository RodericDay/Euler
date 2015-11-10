'''
Find the sum of all the primes below one-hundred thousand
that will never be a factor of R(10**n).
'''

from Euler import prime_sieve

ans = sum(p for p in prime_sieve(100000) if pow(10, 10**20, p)!=1) + 3
print(ans)
