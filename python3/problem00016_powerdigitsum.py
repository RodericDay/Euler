'''
What is the sum of the digits of the number 2^1000?
'''

ans = sum(int(d) for d in str(2**1000))
print(ans)
