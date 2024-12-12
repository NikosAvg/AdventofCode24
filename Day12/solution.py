from collections import defaultdict, deque
import numpy as np
from scipy.ndimage import binary_erosion, label

data = open('test_input.txt').read().strip()

def string_to_array(s):
    # Split the string into lines
    lines = s.splitlines()
    # Convert each line into a list of characters and form a NumPy array
    arr = np.array([list(line) for line in lines])
    return arr



garden = string_to_array(data)
rows, cols = garden.shape

unique = []

for row in range(rows):
    for col in range(cols):
        if garden[row,col] in unique:
           continue
        unique.append(garden[row,col])

res = 0

for u in unique:
    area = np.zeros([rows,cols])
    for row in range(rows):
        for col in range(cols):
            if garden[row,col] == u:
                area[row,col] = 1
    # Ensure the array is boolean
    binary_array = area.astype(bool)
    labeled_array, num_patches = label(binary_array)

    # Define neighbor offsets for 4-connectivity
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for patch_id in range(1, num_patches + 1):
        # Extract the current patch
        patch = (labeled_array == patch_id)

        # Calculate circumference (boundary pixels)
        boundary = patch ^ binary_erosion(patch)

        # Count the edges contributing to the circumference
        circumference = 0
        for x, y in zip(*np.where(boundary)):
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is outside the patch
                if not (0 <= nx < patch.shape[0] and 0 <= ny < patch.shape[1]) or not patch[nx, ny]:
                    circumference += 1
        res += circumference*np.sum(patch)


print(f'Part One {res}')

res2=0

print(f'Part Two {res2}')
