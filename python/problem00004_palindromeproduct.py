'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import itertools as it

three_digit = range(101,1000, 2) # assume end in 9 therefore odd
pairs = it.combinations_with_replacement(three_digit, 2)
products = (a*b for a, b in pairs)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

ans = max(n for n in products if is_palindrome(n))
print(ans)

