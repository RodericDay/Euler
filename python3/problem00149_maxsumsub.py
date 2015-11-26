'''
Looking at the table below, it is easy to verify that the maximum possible sum
of adjacent numbers in any direction (horizontal, vertical, diagonal or
anti-diagonal) is 16 (= 8 + 7 + 1).

    −2    5    3    2
     9   −6    5    1
     3    2    7    3
    −1    8   −4    8

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of
what is known as a "Lagged Fibonacci Generator":

For  1 ≤ k ≤ 55,      sk = [100003 − 200003k + 300007k^3] (mod 1000000) − 500000
For 56 ≤ k ≤ 4000000, sk = [s[k−24] + s[k−55] + 1000000]  (mod 1000000) − 500000

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000
numbers to fill the first row (sequentially), the next 2000 numbers to fill
the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any
direction (horizontal, vertical, diagonal or anti-diagonal).
'''

from itertools import tee

n = 4000000
lim = n**2
s = [None for _ in range(lim)]
for k in range(1, 56):
    s[k-1] = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
for k in range(55, lim):
    s[k] = (s[k-24] + s[k-55] + 1000000) % 1000000 - 500000

assert s[10-1] == -393027
assert s[100-1] == 86613
