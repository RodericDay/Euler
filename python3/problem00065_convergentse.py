'''
What is most surprising is that the important mathematical constant,

    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
'''

from fractions import Fraction

def frac(chain):
    # start at the bottom of the chain, work upwards
    f = Fraction(chain.pop())
    while chain:
        f = chain.pop()+1/f
    return f


if __name__ == '__main__':
    nth = 100
    chain = [2]+[n for k in range(1, 100) for n in (1, 2*k, 1)][:nth-1]
    e = frac(chain)
    ans = sum(int(c) for c in str(e.numerator))
    print(ans)
