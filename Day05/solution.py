import pandas as pd
import io

# Open and read Input
with open('input.txt', 'r') as file:
    data = file.read()
  
#The Plan: Split the input into two strings on an empty line and parse seperatly  
rules, pages = data.split('\n\n')

rules_df = pd.read_csv(io.StringIO(rules), sep="|", header=None)

# Convert to list of lists
list_of_lists = [list(map(int, row.split(','))) for row in pages.split('\n')]

valid_lists = []
for list in list_of_lists:
    valid = False
    prv = list[0]
    tmp = [list[0]]
    for i in range(1,len(list)):
        for index, row in rules_df.iterrows():
            # Check the rules and see if its a valid list
            if prv == row[0] and list[i] == row[1]:
                valid = True
                tmp.append(row[1])
        prv = list[i]
    valid_lists.append(tmp)
    if valid == False:
        continue

res = 0
for list in list_of_lists:
    if list in valid_lists:
        res += list[len(list)//2]
        
print(f'Part One: {res}')


res2 = 0

incorrect_lists = []
# Seperate the wrong lists
for list in list_of_lists:
    if list not in valid_lists:
        incorrect_lists.append(list)

for list in incorrect_lists:
    size = len(list)
    counter=0
    while list not in valid_lists and counter <= size:
        for i in range(1,len(list)):
            for index, row in rules_df.iterrows():
            # Check the rules and see if some pairs are reversed
                if list[i-1] == row[1] and list[i] == row[0]:
                    list[i-1], list[i] = list[i], list[i-1]
    
        counter+=1

    res2 += list[len(list)//2]


print(f'Part Two: {res2}')