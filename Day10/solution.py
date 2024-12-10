import numpy as np
from collections import deque


data = open('input.txt').read().strip()

def string_to_array(s):
    # Split the string into lines
    lines = s.splitlines()
    # Convert each line into a list of characters and form a NumPy array
    arr = np.array([list(line) for line in lines])
    return arr

map = string_to_array(data).astype(int)

possible_starts = deque()
rows, cols  = map.shape

res = 0

for row in range(rows):
    for col in range(cols):
        if map[row,col] == 0:
            possible_paths = deque([(row,col)])
            seen = set()
            while possible_paths:
                curx,cury = possible_paths.popleft()
                if (curx,cury) in seen:
                    continue
                seen.add((curx,cury))
                if map[curx,cury] == 9:
                    res+=1
                for xx,yy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    ccurx, ccury = curx + xx, cury + yy
                    if 0<=ccurx<rows and 0<=ccury<cols and map[ccurx,ccury] == map[curx,cury] + 1:
                        possible_paths.append((ccurx,ccury))


print(f'Part One: {res}')

res2 = 0
# I smell recursion
distinct_paths = {}
def paths(row,col):
    if map[row,col] == 9:
        return 1
    if (row,col) in distinct_paths:
        return distinct_paths[(row,col)]
    r = 0
    for xx,yy in [(-1,0),(0,1),(1,0),(0,-1)]:
        ccurx, ccury = row + xx, col + yy
        if 0<=ccurx<rows and 0<=ccury<cols and map[ccurx,ccury] == map[row,col] + 1:
            r += paths(ccurx,ccury)
    distinct_paths[(row,col)] = r
    return r

for row in range(rows):
    for col in range(cols):
        if map[row,col]==0:
            res2+=paths(row,col)


print(f'Part Two: {res2}')
