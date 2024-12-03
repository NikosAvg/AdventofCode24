import pandas as pd

df = pd.read_csv('input.csv', header=None, sep=" ")
df = df.apply(pd.to_numeric)
List1 = df[0].sort_values()
List2 = df[1].sort_values()
List1 = list(List1)
List2 = list(List2)

# Part one
res = 0
for i1, i2 in zip(List1,List2):
    res += abs(i2-i1)
    
print(res)

res2 = 0
# Part two
for i1 in List1:
    count=0
    for i2 in List2:
        if i1 == i2:
            count+=1
    res2+=i1*count
print(res2)

