'''
See 114.

For m = 3, it can be seen that n = 30 is the smallest value for which
the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and
F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count
function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first
exceeds one million.
'''

import itertools
from problem00114_blockcombinations1 import F

ans = next(n for n in itertools.count() if F(50, n) > 1E6)
print(ans)
