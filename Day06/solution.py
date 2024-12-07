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

positions = ('^','>','v','<')
rows, cols = array.shape
p = np.zeros([rows, cols])


# Start from the initial position
startx, starty = np.where(array == positions[0])

# print((startx[0],starty[0]))
exit = False

posx, posy = startx[0], starty[0]

while exit == False:
    p[posx,posy] = 1
    if array[posx,posy] == positions[0]: # ^
        if posx - 1 < 0:
            exit = True
        elif array[posx - 1,posy] == '#':
            array[posx,posy] = positions[1]
        else:
            array[posx-1,posy],array[posx,posy] = array[posx,posy], array[posx-1,posy]
            posx = posx - 1

    elif array[posx,posy] == positions[1]: # >
        if posy + 1 > cols:
            exit = True
        elif array[posx,posy+1] == '#':
            array[posx,posy] = positions[2]
        else:
            array[posx,posy+1],array[posx,posy] = array[posx,posy], array[posx,posy+1]
            posy = posy + 1
    elif array[posx,posy] == positions[2]: # v
        if posx + 1 >= rows:
            exit = True
        elif array[posx + 1 , posy] == '#':
            array[posx,posy] = positions[3]
        else:
            array[posx + 1,posy],array[posx,posy] = array[posx,posy], array[posx + 1,posy]
            posx = posx + 1
    elif array[posx,posy] == positions[3]: # <
        if posy - 1 < 0:
            exit = True
        elif array[posx,posy - 1] == '#':
            array[posx,posy] = positions[0]
        else:
            array[posx,posy - 1],array[posx,posy] = array[posx,posy], array[posx,posy - 1]
            posy = posy - 1

print(f'Part One: {np.sum(p)}')

# Part Two

# Re initialize the array
array = string_to_array(data)
res2 = 0  # Counter for total loop-causing positions

# Precompute the starting position of the player
startx, starty = np.where(array == positions[0])
startx, starty = startx[0], starty[0]

# Filter relevant positions: only empty positions adjacent to obstacles
relevant_positions = [
    (i, j)
    for i in range(rows)
    for j in range(cols)
    if array[i, j] == '.'
]

for s in relevant_positions:
    # Place the obstacle at position s
    array[s] = '#'

    # Simulate movement directly
    posx, posy = startx, starty
    direction = 0  # Initial direction (0: up, 1: right, 2: down, 3: left)
    visited_states = set()
    exit_sim = False
    loop_detected = False

    while not exit_sim:
        # Detect a loop
        state = ((posx, posy), direction)
        if state in visited_states:
            loop_detected = True
            break

        visited_states.add(state)

        # Determine the next position based on the current direction
        if direction == 0:  # Facing up (^)
            next_posx, next_posy = posx - 1, posy
        elif direction == 1:  # Facing right (>)
            next_posx, next_posy = posx, posy + 1
        elif direction == 2:  # Facing down (v)
            next_posx, next_posy = posx + 1, posy
        elif direction == 3:  # Facing left (<)
            next_posx, next_posy = posx, posy - 1

        # Check bounds
        if not (0 <= next_posx < rows and 0 <= next_posy < cols):
            exit_sim = True
            continue

        # Check for obstacles
        if array[next_posx, next_posy] == '#':
            # Turn right if there's an obstacle
            direction = (direction + 1) % 4
        else:
            # Move forward
            posx, posy = next_posx, next_posy

    # Increment the counter if a loop was detected
    if loop_detected:
        res2 += 1

    # Reset the position
    array[s] = '.'

print(f'Part Two: {res2}')
