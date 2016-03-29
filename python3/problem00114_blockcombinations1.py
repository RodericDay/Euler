'''
A row measuring seven units in length has red blocks with a minimum length of
three units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square. There are exactly
seventeen ways of doing this.

Let the fill-count function, F(m, n), represent the number of ways that a row
can be filled. For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

How many ways can a row measuring fifty units in length be filled?
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def F(s, n):
    return 1 + sum(F(s, n-x-i-1) for i in range(n) for x in range(s, n-i+1))

if __name__ == '__main__':
    ans = F(3, 50)
    print(ans)
