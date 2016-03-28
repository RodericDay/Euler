'''
Consider a brick wall. You want to stack bricks in such a way that there
are no running cracks. Imagine you have bricks of width 2 and 3, how many
possible combinations are there for a wall 32 bricks wide, 10 bricks tall?
'''
import itertools

def recurse1(goal, options=[2, 3]):
    if goal==0:
        yield []
    elif goal>0:
        yield from ([H]+T for H in options for T in recurse1(goal-H))

def W(w, h):
    '''
    >>> W(9, 3)
    8
    '''
    lines = [frozenset(itertools.accumulate(line))-{w} for line in recurse1(w)]
    maps = {a:[b for b in lines if not a & b] for a in lines}
    counts = {a:1 for a in lines}

    for _ in range(h-1):
        temp = counts.copy()
        for a in lines:
            counts[a] = sum(temp[b] for b in maps[a])

    return sum(counts.values())

ans = W(32, 10)
print(ans)
