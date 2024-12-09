
data = open('test_input.txt').read().strip()

d = []
ID = 0
for i in range(len(data)):
    if i%2 == 0:
        for s in range(int(data[i])):
            d.append(f'{ID}')
        ID+=1
    else:
        for s in range(int(data[i])):
            d.append('.')

d2 = d.copy()
for i in range(len(d)):
    if d[i] == '.':
        for j in range(len(d)-1, i,-1):
            if d[j] != '.':
                d[i], d[j] = d[j], d[i]
                break

res = 0
end = 0
for i in range(len(d)):
    if d[i] == '.':
        end = i
        break

for i in range(end):
    res += i*int(d[i])

print(f'Part One {res}')
