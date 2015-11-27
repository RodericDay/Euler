'''
What is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
'''

from Euler import is_prime, itertools

# consider a layer N
# for example, N = 3
# .......         .......
# .NNNNN.    S    .C...C.
# .N...N.    S    ..XXXX.
# .N...N. => S => ..XXXX.
# .N...N.    S    ..XXXX.
# .NNNNN.    S    .C.....
# .......         .......

count = 0
for N in itertools.count(start=2):
    S = 2*N-1
    X = (S-1)*(S-2)
    i = X+1
    count += sum(is_prime(i+j*(S-1)) for j in range(3))
    total = 4*N-3
    if count/total < 0.1:
        break

ans = S
print(ans)
