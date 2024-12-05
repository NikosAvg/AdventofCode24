import pandas as pd
import io

# Open and read Input
with open('input.txt', 'r') as file:
    data = file.read()

# The Plan: Split the input into two strings on an empty line and parse separately
rules, pages = data.split('\n\n')

rules_df = pd.read_csv(io.StringIO(rules), sep="|", header=None)

# Convert rules to a set of tuples for fast lookup
rule_set = set((row[0], row[1]) for _, row in rules_df.iterrows()) # list to set -> O(n) to O(1) lookup time!!!!

# Convert pages to list of lists
list_of_lists = [list(map(int, row.split(','))) for row in pages.split('\n')]

valid_lists = []
valid_set = set()
res = 0

# Validate lists using the rules
for lst in list_of_lists:
    valid = True
    tmp = [lst[0]]
    for i in range(1, len(lst)):
        if (lst[i - 1], lst[i]) in rule_set:
            tmp.append(lst[i])
        else:
            valid = False
            break # Avoiding Unnecessary iterations
    if valid:
        valid_lists.append(tmp)
        valid_set.add(tuple(lst))
        res += lst[len(lst) // 2]

print(f'Part One: {res}')

# Part Two: Handle incorrect lists
res2 = 0
for lst in list_of_lists:
    if tuple(lst) not in valid_set:
        size = len(lst)
        counter = 0
        lst_valid = False
        while not lst_valid and counter <= size:
            for i in range(1, len(lst)):
                if (lst[i], lst[i - 1]) in rule_set:
                    lst[i], lst[i - 1] = lst[i - 1], lst[i]
            # Check if the modified list is valid
            tmp = [lst[0]]
            lst_valid = True
            for i in range(1, len(lst)):
                if (lst[i - 1], lst[i]) in rule_set: # Reverse only pairs that are valid
                    tmp.append(lst[i])
                else:
                    lst_valid = False
                    break
            counter += 1
        if lst_valid:
            res2 += lst[len(lst) // 2]

print(f'Part Two: {res2}')
