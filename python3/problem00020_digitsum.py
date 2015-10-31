'''
Find the sum of the digits in the number 100!
'''

from math import factorial

ans = sum(map(int,str(factorial(100))))
print(ans)
