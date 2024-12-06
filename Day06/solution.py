import numpy as np
# Open and read Input
with open('test_input.txt', 'r') as file:
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
