'''
Same as 137, but the series F is instead

    Fk = Fk−1 + Fk−2
    F1 = 1
    F2 = 4

Golden nugget 20 is 211345365.
Find the sum of the first 30 golden nuggets.
'''

G = (1+5**0.5)/2;

x = 0
ans = 0
seen = set()
for d in range(1, 10000000):
    for n in range(int(x*d) or 1, int(d/G)+1):
        N = 3*n*n+n*d
        D = d*d-n*d-n*n
        if (N%D==0):
            A = N//D
            if A not in seen:
                seen.add(A)
                ans += A
                i = len(seen)
                if i%2==0:
                    x = n/d
                    if i==30:
                        print(ans)
                        exit()
