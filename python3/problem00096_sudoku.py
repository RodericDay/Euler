'''
The 6K text file, sudoku.txt contains fifty different Su Doku puzzles ranging
in difficulty, but all with unique solutions.

By solving all fifty puzzles, find the sum of the 3-digit numbers found in the
top left corner of each solution grid. For example, 483 is the 3-digit number
found in the top left corner of the solution grid above.
'''

import re
from itertools import chain
import functools as ft

@ft.lru_cache(maxsize=81)
def neighbors(i):
    row = range(i//9*9, i//9*9+9)
    col = range(i%9, 81, 9)
    box = (i//27*27+i%9//3*3+j+k*9 for j in range(3) for k in range(3))
    return set(chain(row, col, box))

def solve(string):
    sudoku = list(string)
    mem = {idx:set('123456789')-{sudoku[j] for j in neighbors(idx)}
            for idx, val in enumerate(sudoku) if val=='0'}

    while '0' in sudoku:
        idx, opts = min(mem.items(), key=lambda t: len(t[1]))
        try:
            val, = opts # unpack set
            sudoku[idx] = val
            for j in neighbors(idx):
                if j in mem:
                    mem[j] -= {val}
            mem.pop(idx)
        except ValueError:
            for val in opts:
                copy = list(sudoku)
                copy[idx] = val
                try:
                    return solve(copy)
                except RuntimeError:
                    continue
            raise RuntimeError

    return ''.join(sudoku)


with open('../resources/p096_sudoku.txt') as fp:
    text = fp.read().replace('\n', '')

ans = 0
for string in re.findall(r'Grid \d\d([\d]{81})', text):
    ans += int(solve(string)[:3])
print(ans)
