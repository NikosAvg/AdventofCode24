import numpy as np
from collections import defaultdict
# Open and read Input
with open('input.txt', 'r') as file:
    data = file.read()

def string_to_array(s):
    # Split the string into lines
    lines = s.splitlines()
    # Convert each line into a list of characters and form a NumPy array
    arr = np.array([list(line) for line in lines])
    return arr

map = string_to_array(data)

rows, cols = map.shape
P = defaultdict(list)

# Rules
# An antinode occurs at any point that is perfectly in line with two antennas of the same frequency
# but only when one of the antennas is twice as far away as the other
res = 0

# Find All Antennas
for row in range(rows):
    for col in range(cols):
        if map[row,col] != '.':
            P[map[row,col]].append((row,col))

# Initialize Sets for Answers for part one and two
A1 = set()
A2 = set()

# Brute Force it
for row in range(rows):
    for col in range(cols):
        for key, vals in P.items():
            for (r1, c1) in vals:
                for (r2, c2) in vals:
                    if (r1,c1) != (r2,c2):
                        # To check if our (row,col), (r1,c1) and (r2,c2) are in one line we check the slopes of
                        # (row,col) - (r1,c1) and (row,col) - (r2,c2) to be the same
                        d1 = abs(row - r1) + abs(col - c1)
                        d2 = abs(row - r2) + abs(col - c2)

                        dr1 = row - r1
                        dr2 = row - r2
                        dc1 = col - c1
                        dc2 = col - c2

                        if (d1 == 2*d2 or d1*2 == d2) and 0<=row<rows and 0<=col<cols and (dr1*dc2 == dr2*dc1):
                            A1.add((row,col))
                        if 0<=row<rows and 0<=col<cols and (dr1*dc2 == dr2*dc1):
                            A2.add((row,col))

res = len(A1)
res2 = len(A2)

print(f'Part One {res}')
print(f'Part Two {res2}')
