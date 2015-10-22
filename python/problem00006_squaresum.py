'''
Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
'''

sum_squares = sum(n**2 for n in range(101))
square_sums = sum(range(101))**2

ans = abs(sum_squares - square_sums)
print(ans)
