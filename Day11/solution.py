from collections import deque

data = open('input.txt').read().strip().split(' ')
def parse_stone(stone,new_stones):
    if int(stone) == 0:
        new_stones.append(str(1))
    elif len(stone) % 2 == 0:
        l_stone = int(stone[:len(stone)//2])
        r_stone = int(stone[len(stone)//2:])
        new_stones.append(str(l_stone))
        new_stones.append(str(r_stone))
    else:
        stone = str(int(stone) * 2024)
        new_stones.append(stone)


blinks = 25
for blink in range(blinks):
    new_stones = deque()
    for d in data:
        parse_stone(d,new_stones)
    data = list(new_stones)
res = len(data)

print(f'Part One {res}')

data = open('input.txt').read().strip().split(' ')
res2 = 0
blinks = 75
for blink in range(blinks):
    new_stones = deque()
    for d in data:
        parse_stone(d,new_stones)
    data = list(new_stones)
res = len(data)

print(f'Part Two {res2}')
