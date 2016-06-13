import numpy as np

S, l = np.arange(1, 101)**2, 50 # 115039000
# S, l = np.array([1, 3, 6, 8, 10, 11]), 3
k = S.sum()
idxs = np.arange(k)

M = np.zeros([l+1, k], dtype='int32')
M[0,0] = 1

for s in S:
    for j in range(l-1,-1,-1):
        row = M[j]
        cols = idxs[row>0]
        M[j+1, s+cols] += M[j, cols]

ans = idxs[M[l]==1].sum()
print(ans)
