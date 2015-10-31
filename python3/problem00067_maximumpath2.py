'''
Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

This is a much more difficult version of Problem 18.
'''

from problem00018_maximumpath1 import maximum_path

with open('../resources/p067_triangle.txt') as fp:
    ans = maximum_path(fp.read())

print(ans)
