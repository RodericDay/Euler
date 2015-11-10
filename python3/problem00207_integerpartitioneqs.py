'''
For some positive integers k, there exists an integer partition of the form

    4^t = 2^t + k

where 4^t, 2^t, and k are all positive integers and t is a real number.

The first two such partitions are

    4^1 = 2^1 + 2
    4^1.5849625... = 2^1.5849625... + 6

Partitions where t is also an integer are called perfect.

For any m ≥ 1 let P(m) be the proportion of such partitions
that are perfect with k ≤ m.

Thus P(6) = 1/2.

In the following table are listed some values of P(m)

    P(5) = 1/1
    P(10) = 1/2
    P(15) = 2/3
    P(20) = 1/2
    P(25) = 1/2
    P(30) = 2/5
    ...
    P(180) = 1/4
    P(185) = 3/13

Find the smallest m for which P(m) < 1/12345
'''

# solution i exists for m = i * ( i - 1 )
# the solution is perfect if i is of form 2^x
p = 1
i = 2
n = 4

while not p / i < 1 / 12345:

    if i == n:
        n *= 2
        p += 1

    i += 1

i += 1 # th answer
ans = m = i*(i-1)
print(ans)
