'''
Consider

    A(x) = xF1 + x2F2 + x3F3 + ...

where Fk is the kth term in the Fibonacci sequence:

    Fk = Fk−1 + Fk−2
    F1 = 1
    F2 = 1

For which values of x is A(x) a positive integer?

    x      AF(x)
  √2−1      1
   1/2      2
(√13−2)/3   3
(√89−5)/8   4
(√34−3)/5   5

A(x) is a golden nugget if x is rational. The 10th golden nugget is 74049690.
Find the 15th golden nugget.
'''

G = (1+5**0.5)/2;

count = 0
max_seen = 0
max_frac = 0
for d in range(1, 10000000):
    for n in range(int(max_frac*d), int(d/G)+1):
        N = n*d
        D = d*d-n*d-n*n
        if (N%D==0):
            A = N//D
            if A > max_seen:
                count += 1
                max_seen = A
                max_frac = n/d
                if count == 15:
                    print(A)
                    exit()
