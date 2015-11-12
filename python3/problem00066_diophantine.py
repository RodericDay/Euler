'''
Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

Assume there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5...}, we obtain the following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
  > 9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

Hence, for D ≤ 6, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x
for which the largest value of x is obtained.
'''

from problem00064_oddperiodsqrt import cfrac
from problem00065_convergentse import frac
from itertools import cycle, chain

def Pell(D):
    a, *repeat = cfrac(D)
    if not repeat: return 0
    g = chain([a], cycle(repeat))
    seen = []
    while True:
        seen.append(next(g))
        f = frac(seen[:])
        x = f.numerator
        y = f.denominator
        if x**2 - D*y**2 == 1:
            return x


ans = max(range(1000), key=Pell)
print(ans)
