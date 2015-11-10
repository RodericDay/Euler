'''
Find the sum of all the primes below two million.
'''

from Euler import prime_sieve

ans = sum(prime_sieve(2*10**6))
print(ans)
