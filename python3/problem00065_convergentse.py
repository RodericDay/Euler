'''
What is most surprising is that the important mathematical constant,

    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
'''

from itertools import cycle
from fractions import Fraction

def convergents(chain):
    first, *rest = chain
    repeating = cycle(rest)
    f = Fraction(first)
    m = next(repeating)
    fn = Fraction(1 + f*m, m)
    for m in repeating:
        yield f
        n = f.numerator   + m * fn.numerator
        d = f.denominator + m * fn.denominator
        f, fn = fn, Fraction(n, d)


if __name__ == '__main__':
    chain = [2] + [n for k in range(1, 100) for n in (1, 2*k, 1)]
    g = convergents(chain)
    f = next(f for i, f in enumerate(g) if i==100-1) # getting 100th
    ans = sum(int(c) for c in str(f.numerator))
    print(ans)
