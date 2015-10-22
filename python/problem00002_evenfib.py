'''
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''

import itertools

def fibonacci():
    a, b = 2, 1
    while True:
        yield b
        a, b = a+b, a

def fibonacci_upto(n):
    below_n = lambda n: n < 4E6
    yield from itertools.takewhile(below_n, fibonacci())


if __name__ == '__main__':
    ans = sum(n for n in fibonacci_upto(4E6) if n%2==0)
    print(ans)
