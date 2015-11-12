'''
All square roots are periodic when written as continued fractions
and can be written in the form:

   √N = a0 +   1
            ----------------
            a1 +   1
                ------------
                a2 +   1
                    --------
                    a3 + ...

For example, let us consider √23:

If we continue we would get the following expansion:

  √23 =  4 +   1
            -------------------
            1 +   1
                ---------------
                3 +   1
                    -----------
                    1 +   1
                        -------
                        8 + ...

The process can be summarised as follows:

              1      √23+4         √23—3
    a0 = 4, ----- = -------- = 1 + -----
            √23—4       7            7

              7     7(√23+3)       √23—3
    a1 = 1, ----- = -------- = 3 + -----
            √23—3      14            2

              2     2(√23+3)       √23-4
    a2 = 3, ----- = -------- = 1 + -----
            √23—3      14            7

              7     7(√23+4)       √23+4
    a3 = 1, ----- = -------- = 1 + -----
            √23—4       7            1

              1     1(√23+4)       √23+4
    a4 = 8, ----- = -------- = 1 + ----- (Seen!)
            √23—4       7            7

It can be seen that the sequence is repeating. For conciseness, we use the
notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats.

The first ten continued fraction representations of square roots are:

     √2 = [1;(2)],          period=1
     √3 = [1;(1,2)],        period=2
     √5 = [2;(4)],          period=1
     √6 = [2;(2,4)],        period=2
     √7 = [2;(1,1,1,4)],    period=4
     √8 = [2;(1,4)],        period=2
    √10 = [3;(6)],          period=1
    √11 = [3;(3,6)],        period=2
    √12 = [3;(2,6)],        period=2
    √13 = [3;(1,1,1,1,6)],  period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
'''

from itertools import count
from math import sqrt, floor

def cfrac(S):
    alist = []
    seen = set()
    m = m0 = 0
    d = d0 = 1
    a = a0 = floor(sqrt(S))
    if a0**2 == S: return [a0]
    while (m, d, a) not in seen:
        seen.update({(m, d, a)})
        alist.append(a)
        m = d*a - m
        d = ( S - m**2 ) // d
        a = ( a0 + m ) // d
    return alist


if __name__ == '__main__':
    ans = sum(len(l)%2==0 for l in map(cfrac, range(10000)))
    print(ans)