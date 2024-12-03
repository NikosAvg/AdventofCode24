
import numpy as np

lines = []
with open('input.txt') as file:
    for line in file:
        l =  line.rstrip().split()
        l = [int(i) for i in l]
        lines.append(l)

def check_conditions(line):
    ascending = all(line[i] <= line[i+1] for i in range(len(line) - 1))
    descending = all(line[i] >= line[i+1] for i in range(len(line) - 1))
    dist = all(1 <= np.abs(line[i] - line[i+1]) <= 3 for i in range(len(line) - 1))
    return ascending or descending, dist

# Part one
res = 0
for line in lines:
    # Check Asc or Dec and Dist
    asc_desc, dist = check_conditions(line)
    if asc_desc and dist:
        res+=1
print(f'Part One: {res}')

# Part 2
res2 = 0
for line in lines:
    while True:
        asc_desc, dist = check_conditions(line)
        if asc_desc and dist:
            # If the line satisfies all conditions, increment counter and break
            res2 += 1
            break

        # Try removing one element at a time
        fixed = False
        for i in range(len(line)):
            temp_line = line[:i] + line[i+1:]  # Temporarily remove element at index i
            asc_desc, dist = check_conditions(temp_line)
            if asc_desc and dist:
                # If removing this element fixes the line, make the change permanent
                line = temp_line
                fixed = True
                break

        # If no single removal fixes the line, stop trying
        if not fixed:
            break

print(f"Part Two: {res2}")