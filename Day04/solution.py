import numpy as np

# Open and read Input
with open('input.txt', 'r') as file:
    data = file.read()
    
def string_to_array(s):
    # Split the string into lines
    lines = s.splitlines()
    
    # Convert each line into a list of characters and form a NumPy array
    arr = np.array([list(line) for line in lines])
    return arr


array = string_to_array(data)            

rows, cols = array.shape
groups = []

for r in range(rows):
    for c in range(cols - 3):
         groups.append(array[r, c:c+4])
        
for r in range(rows - 3):
    for c in range(cols):     
         groups.append(array[r:r+4, c])

for r in range(rows - 3):
    for c in range(cols - 3):
        groups.append([array[r+i, c+i] for i in range(4)])
        
for r in range(rows - 3):
    for c in range(3, cols):  # Start at index 3 to ensure enough elements on the left
        groups.append([array[r+i, c-i] for i in range(4)])
        
        
groups = [''.join(row) for row in groups]

res = 0
for g in groups:
    if g == 'XMAS' or g == 'SAMX':
        res+=1

print(f'Part One: {res}')

# Change Optics for Part Two

# Main Idea: Split the large array into smaller 3x3 arrays and check the condition.
def check_x_condition(array):
    # Check main and secondary diagonal for the condition
    main = array[0,0] + array[1,1] + array[2,2]
    secondary = array[0,2] + array[1,1] + array[2,0]
    if (main == 'MAS' or main == 'SAM') and (secondary == 'MAS' or secondary == 'SAM'):
        return 1

    return 0 


res2 = 0
for r in range(rows-2):
    for c in range(cols - 2):
        res2 += check_x_condition(array[r:r+3,c:c+3])


print(f'Part Two: {res2}')