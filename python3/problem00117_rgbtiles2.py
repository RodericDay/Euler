'''
Using a combination of black square tiles and oblong tiles chosen from the same
pool as 116, it is possible to tile a row measuring five units in length in
exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def H(m):
    if m <= 0:
        return m == 0
    return sum(H(m-s) for s in ss) + H(m-1)

ss = [2, 3, 4]
ans = H(50)
print(ans)
