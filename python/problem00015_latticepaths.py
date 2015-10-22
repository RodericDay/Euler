'''
Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

from math import factorial

x, y = 20, 20
# to get from point A to point B you need x+y displacements in total
moves = factorial(x+y)
# however, some moves will result in identical paths, so prune
moves = moves // factorial(x) // factorial(y)
print(moves)
