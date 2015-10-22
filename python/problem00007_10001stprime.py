'''
What is the 10,001st prime number?
'''

from problem00003_primefactor import prime_sieve

def nth(iterable, n):
    for i, value in enumerate(iterable):
        if i==n: return value
    raise RuntimeError("Iterable length {} < {}".format(i, n))


if __name__ == '__main__':
    ans = nth(prime_sieve(200000), 10000)
    print(ans)
