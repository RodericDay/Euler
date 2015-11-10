'''
Taking three different letters from the 26 letters of the alphabet, character
strings of length three can be formed. Examples are 'abc', 'hat' and 'zyx'.

When we study these three examples we see that for 'abc' two characters come
lexicographically after its neighbour to the left. For 'hat' there is exactly
one character that comes lexicographically after its neighbour to the left.
For 'zyx' there are zero characters that come lexicographically after its
neighbour to the left.

In all there are 10400 strings of length 3 for which exactly one character
comes lexicographically after its neighbour to the left.

We now consider strings of n ≤ 26 different characters from the alphabet.
For every n, p(n) is the number of strings of length n for which exactly one
character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?
'''

from math import factorial
import functools

def C(n, k):
    ''' binomial(n, k) '''
    return factorial(n)//factorial(k)//factorial(n-k)

@functools.lru_cache(maxsize=None)
def T(n, k):
    ''' triangle of eulerian numbers '''
    if n<1: return 0
    if n==k: return 1
    return k * T(n-1, k) + (n-k+1) * T(n-1, k-1)

n = 26
pascal_row = [C(n, k) for k in range(2, n+1)]
euler_row = [T(k, 2) for k in range(2, n+1)]
my_row = [a*b for a, b in zip(pascal_row, euler_row)]
ans = max(my_row)
print(ans)
