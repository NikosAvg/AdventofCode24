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

def parse_stone2(stone, blink):
    stone = int(stone)
    # return the length of the list after one stone has been parsed x times
    if (stone, blink) in dp:
        return dp[(stone, blink)]
    if blink == 0:
        ret = 1
    elif stone == 0:
        ret = parse_stone2(1, blink-1)
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone))//2
        l_stone = str(stone)[:mid]
        r_stone = str(stone)[mid:]
        ret = parse_stone2(int(l_stone), blink-1) + parse_stone2(int(r_stone), blink-1)
    else:
        ret = parse_stone2(stone*2024,blink-1)
    dp[(stone, blink)] = ret
    return ret

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
res2=0
data = open('input.txt').read().strip().split(' ')
blinks = 75
for d in data:
    res2 += parse_stone2(d,blinks)


print(f'Part Two {res2}')
