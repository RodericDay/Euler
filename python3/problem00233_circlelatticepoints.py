'''
Let f(N) be the number of points with integer coordinates that are on a circle passing through

    (0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?
'''

def f(N):
    N = 10000
    r = (2*N*N)**0.5/2
    d = r-N/2
    s = 0
    for x in range(int(-d), int(2*r-d)+1):
        xr2 = (x-N/2)**2
        yr2 = (r**2 - xr2)
        y = yr2**0.5+N/2
        if y.is_integer():
            s += 2
            # print(x, x, y, N-y)
    return s

ans = f(10000)
print(ans)
