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

import itertools

def p_(n, N):
    count = 0
    for combo in itertools.permutations(range(N), n):
        count += sum(a>b for a, b in zip(combo, combo[1:]))==1
    return count

for N in range(2, 8):
    print([p_(n, N) for n in range(2, N+1)])

# [1]
# [3, 4]
# [6, 16, 11]
# [10, 40, 55, 26]
# [15, 80, 165, 156, 57]
# [21, 140, 385, 546, 399, 120]
# goal: find max of row 26
