import re
# Open and read Input
with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
# Regular expression to match mul(Number, number)
pattern = r"mul\((-?\d*\.?\d+),\s*(-?\d*\.?\d+)\)"

# Find all matches
matches = re.findall(pattern, data)

res = 0
# Print results
for match in matches:
    res += int(match[0])*int(match[1])
    
print(f'Part One: {res}')


# Step 1: Mask everything between don't() and do()
exclude_pattern = r"don't\(\).*?do\(\)"
masked_input = re.sub(exclude_pattern, "", data, flags=re.DOTALL)

# Step 2: Find all valid mul(Number, Number) patterns in the remaining text
matches = re.findall(pattern, masked_input)
res2=0

for match in matches:
    res2 += int(match[0])*int(match[1])
    
# Print results
print(f'Part Two: {res2}')