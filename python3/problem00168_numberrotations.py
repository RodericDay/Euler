'''
It can be verified that 714285 = 5 × 142857.
This demonstrates that 142857 is a divisor of its right-rotation.
Find the last 5 digits of the sum of all integers n

    10 < n < 10100

that have this property.
'''

def period(n, d, t=0):
    if n == 9 and d == 9: return '9'
    seen, p = set(), ''
    while (n, t) not in seen:
        p += str(t)
        seen.add((n, t))
        n = (n%d) * 10
        t = n//d
    return p[1:]

def concat(s, lim):
    x, i = 0, 1
    while x < lim:
        yield x
        x, i = int(s*i), i+1

ans = 0
for k in range(1, 10):
    for i in range(k, 10):
        d = 10*k - 1
        p = period(i, d)
        ans += sum(n for n in concat(p, 10**100) if n > 10)
print(ans%10**5)

