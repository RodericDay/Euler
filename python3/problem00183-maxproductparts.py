'''
N = 11 -> Pmax = (11/4)^4; M(11) = 14641/256 = 57.19140625
N =  8 -> M(8) = 512/27

D(N) = N if M(N) is a non-terminating decimal else -N.

For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

Find ΣD(N) for 5 ≤ N ≤ 10000.
'''

from fractions import Fraction, gcd
from functools import lru_cache

@lru_cache(maxsize=None)
def non_terminating_decimal(M):
    D = M.denominator
    while D%2==0:
        D //= 2
    while D%5==0:
        D //= 5
    return D != 1

ans = 0
k = 2
f = lambda N, k: Fraction(N, k)**k
for N in range(5, 10001):
    A, B = f(N, k), f(N, k+1)
    M = max(A, B)
    if B > A: k += 1
    ans += N if non_terminating_decimal(M) else -N
print(ans)
