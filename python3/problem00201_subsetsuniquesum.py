from collections import defaultdict

S, l = [n*n for n in range(1, 101)], 50
# S, l = [1, 3, 6, 8, 10, 11], 3

table = defaultdict(dict)
table[0][0] = False  # the 0-length 0-sum combination is not a dupe

for s in S:
    for k in range(l-1,-1,-1):
        for s0, is_dupe in table[k].items():
            table[k+1][s0+s] = is_dupe or s0+s in table[k+1]

ans = sum(s for s, is_dupe in table[l].items() if not is_dupe)
print(ans)
