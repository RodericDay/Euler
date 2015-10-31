'''
Find the sum of all the primes below two million.
'''

from problem00003_primefactor import prime_sieve

ans = sum(prime_sieve(2*10**6))
print(ans)
