from collections import defaultdict, deque

data = open('input.txt').read().strip().split(' ')

def parse_stone(stone,dp):
    if stone in dp:
        return dp[stone]

    if int(stone) == 0:
        dp[stone] = ['1']
    elif len(stone) % 2 == 0:
        l_stone = int(stone[:len(stone)//2])
        r_stone = int(stone[len(stone)//2:])
        dp[stone] = [str(l_stone), str(r_stone)]
    else:
        dp[stone] = [str(int(stone) * 2024)]

    return dp[stone]

dp = {}
blinks = 25
for _ in range(blinks):
    new_stones = deque()
    for d in data:
        new_stones.extend(parse_stone(d,dp))
    data = list(new_stones)
res = len(data)

print(f'Part One {res}')
dp = {}
data = open('input.txt').read().strip().split(' ')
blinks = 75
for _ in range(blinks):
    new_stones = deque()
    for d in data:
        new_stones.extend(parse_stone(d,dp))
    data = list(new_stones)
res2 = len(data)

print(f'Part Two {res2}')
