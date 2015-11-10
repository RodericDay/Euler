'''
[See 129]

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime
factors is 9414.

Find the sum of the first forty prime factors of R(10**9).
'''

from Euler import prime_sieve

# any factor of 111...[k] is also a factor of 999...[k]
# and 999...[k] is 10**k-1. so if the remainder is 1, the number is a factor
# however, skip 3, since it trivially divides 9
found = [p for p in prime_sieve(2E5) if pow(10, 10**9, p)==1][1:41]
assert len(found) == 40
ans = sum(found)
print(ans)
