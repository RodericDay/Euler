'''
A row of five black square tiles is to have a number of its tiles replaced with
coloured oblong tiles chosen from red (length two), green (length three), or
blue (length four).

How many different ways can the black tiles in a row measuring fifty units in
length be replaced if colours cannot be mixed and at least one coloured tile
must be used?

G(5) = 12
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def G(s, n):
    return 1 + sum(G(s, n-x-i-1) for i in range(n) for x in range(s, n-i+1, s))

if __name__ == '__main__':
    ans = G(2, 50) + G(3, 50) + G(4, 50) - 3
    print(ans)
