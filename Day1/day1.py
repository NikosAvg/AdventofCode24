import math
import pandas as pd

df = pd.read_csv('input.csv', header=None, sep=" ")
df = df.apply(pd.to_numeric)
l1 = df[0].sort_values()
l2 = df[1].sort_values()
l1 = list(l1)
l2 = list(l2)

res = 0
for i1, i2 in zip(l1,l2):
    res += abs(i2-i1)
    
print(res)