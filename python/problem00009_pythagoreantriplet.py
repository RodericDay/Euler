'''
A Pythagorean triplet is a set of three natural numbers,

    a < b < c

for which,

    a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for c in range(1000, 0, -1):
    for b in range(c, 0, -1):
        a = 1000 - b - c
        if a > 0 and a**2 + b**2 == c**2:
            ans = a * b * c
            print(ans)
            exit()
