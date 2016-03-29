'''
A row measuring seven units in length has red blocks with a minimum length of
three units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square. There are exactly
seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?
'''

def ways(total, cache={}):
    if total in cache: return cache[total]

    count = 0

    for start in range(total):
        for size in range(3, total-start+1):
            left = total-size-start
            if left > 3:
                m = ways(left-1)
            else:
                m = 1
            count += m

    cache[total] = count + 1
    return cache[total]

ans = ways(50)
print(ans)
