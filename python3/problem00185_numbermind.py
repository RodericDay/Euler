import random
from itertools import combinations, accumulate
from collections import defaultdict, Counter

import re
with open('../resources/p185_numbermind.txt') as fp:
    known = [(a, int(b)) for a, b in (re.findall(r'\d+', line) for line in fp)]

_known = [
  ('90342', 2),
  ('70794', 0),
  ('39458', 2),
  ('34109', 1),
  ('51545', 2),
  ('12531', 1),
] # 39542

def knapsack(goals, carry=''):
    i = len(carry)
    if i==3:
        print(carry)

    if all(g==0 for g in goals):
        return carry

    for j in range(10):
        new_goals = []
        for guess, goal in zip(guesses, goals):
            n = goal - (str(j)==guess[i])
            if n < 0: break
            new_goals.append(n)
        else:
            new_carry = carry + str(j)
            if sum(new_goals) > acc[i+1]: continue
            ans = knapsack(new_goals, new_carry)
            if ans: return ans

guesses, goals = list(zip(*known))
size = len(guesses[0])
contrib = [[sum(g[index]==c for g in guesses) for c in '0123456789']
            for index in range(size)]
acc = list(accumulate([max(l) for l in contrib[::-1]]))[::-1]+[0]
ans = knapsack(goals)
print(ans)
