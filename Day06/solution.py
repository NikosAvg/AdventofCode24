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

# Simulation function
def simulate_movement(array, startx, starty, modify_array=False, block_pos=None):
    rows, cols = array.shape
    positions = ('^', '>', 'v', '<')
    direction = 0  # Start facing up
    posx, posy = startx, starty
    p = np.zeros([rows, cols])  # Track visited positions
    visited_states = set()
    exit_sim = False
    loop_detected = False

    if modify_array and block_pos is not None:
        array[block_pos] = '#'

    while not exit_sim:
        # Detect a loop
        state = ((posx, posy), direction)
        if state in visited_states:
            loop_detected = True
            break

        visited_states.add(state)
        p[posx, posy] = 1  # Mark position as visited

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
            array[posx, posy] = positions[direction]
        else:
            # Move forward
            array[posx, posy], array[next_posx, next_posy] = array[next_posx, next_posy], array[posx, posy]
            posx, posy = next_posx, next_posy

    if modify_array and block_pos is not None:
        array[block_pos] = '.'  # Reset the position if modified

    return np.sum(p), loop_detected

# Prepare the array
array = string_to_array(data)
rows, cols = array.shape
startx, starty = np.where(array == '^')
startx, starty = startx[0], starty[0]

# Part One
res, _ = simulate_movement(array.copy(), startx, starty)
print(f'Part One: {res}')

# Part Two
relevant_positions = [
    (i, j)
    for i in range(rows)
    for j in range(cols)
    if array[i, j] == '.'
]

res2 = 0  # Counter for total loop-causing positions

for block_pos in relevant_positions:
    _, loop_detected = simulate_movement(array.copy(), startx, starty, modify_array=True, block_pos=block_pos)
    if loop_detected:
        res2 += 1
print(f'Part Two: {res2}')
