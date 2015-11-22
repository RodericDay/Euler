'''
N = 11 -> Pmax = (11/4)^4; M(11) = 14641/256 = 57.19140625
N =  8 -> M(8) = 512/27

D(N) = N if M(N) is a non-terminating decimal else -N.

For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

Find ΣD(N) for 5 ≤ N ≤ 10000.
'''

from math import log

ans = 0
k = 1
f = lambda N, k: k * log(N/k)
for N in range(5, 10001):
    A, B = f(N, k), f(N, k+1)
    M = max(A, B)
    if B > A:
        k += 1
        r = k
        while r%2==0: r//=2
        while r%5==0: r//=5
    ans += N if N%r else -N
print(ans)
