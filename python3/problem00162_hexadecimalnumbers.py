'''
Hexadecimal numbers are represented using 16 different digits:

    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

In 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
We write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist
with all of the digits 0,1, and A present at least once?
Give your answer as an uppercase hexadecimal number.
'''

N = 16
# S = 0
# for n in range(16**N):
#     s = "{:x}".format(n)
#     if set('0bc') <= set(s):
#         S += 1
# print(S)

def k(s, m=3, z=1):
    '''
    knapsack: spots and missing figures and leading zero
    '''
    if m==0:
        return 16**s
    if s==0:
        return 0
    return (m-z)*k(s-1, m-1, 0) + (16-m)*k(s-1, m, 0) + z*k(s-1, m, z)

ans = k(N)
print("{:X}".format(ans))
