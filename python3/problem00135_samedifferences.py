'''
Given the positive integers, x, y, and z, are consecutive terms of an
arithmetic progression, the least value of the positive integer, n, for which
the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

    34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
'''

# (2xa+a2) - (x2-2xa+a2)

def f(x, a):
    return 6*x*a - x**2 - 5*a**2

def g(lim, nsol):
    a = 0
    counter = [0 for _ in range(lim)]
    while True:
        a += 1
        if 2*a+1 > lim and f(5*a-1, a) > lim:
            break

        # rainbow from left
        for x in range(2*a+1, 3*a+1):
            y = f(x, a)
            if y >= lim:
                break
            counter[y] += 1

        # rainbow from right
        for x in range(5*a-1, 3*a, -1):
            y = f(x, a)
            if y >= lim:
                break
            counter[y] += 1

    return counter.count(10)

if __name__ == '__main__':
    ans = g(1000000, 10)
    print(ans)
