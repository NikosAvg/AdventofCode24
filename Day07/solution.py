from itertools import product, combinations
import operator

# Initialize an empty dictionary
data_dict = {}

operations = {
    '+': operator.add,
    '*': operator.mul,
    '|': None,
}
def generate_combinations(x, num_operators=2, type=0):
    if type==0:
        operators = ['+', '*']
    else:
        operators = ['+', '*', '|']

    operator_combinations = []

    # Generate combinations for the given number of operators
    for pos_tuple in combinations(range(x), num_operators):  # Choose `num_operators` distinct positions
        for operator_tuple in product(operators, repeat=num_operators):  # All combinations of the operators
            combo = ['' for _ in range(x)]  # Empty positions
            for idx, pos in enumerate(pos_tuple):
                combo[pos] = operator_tuple[idx]  # Place operators in selected positions
            operator_combinations.append(''.join(combo))

    # If no combinations are generated, return a single operator as fallback
    if len(operator_combinations) == 0:
        return operators

    return operator_combinations

# Open and read Input as a dictionary
with open('input.txt', 'r') as file:
    for line in file:
            # Split the line into key and value
            key, value = line.split(':')
            # Strip whitespace and split the values into a list of integers
            data_dict[int(key.strip())] = list(map(int, value.strip().split()))

res = 0
for key in data_dict:
    combinations_list = generate_combinations(len(data_dict[key])-1, len(data_dict[key])-1, type=0)
    for combination in combinations_list:
        # Corectly initialize based on the first operator:
        if len(combination) == 1:
            ans = data_dict[key][0]
            for d in data_dict[key][1:]:
                ans = operations[combination](ans,d)
        else:
            ans = data_dict[key][0]
            for d,c in zip(data_dict[key][1:],combination):
                ans = operations[c](ans,d)
        if ans == key:
            res += key
            break
print(f'Part One = {res}')

res2 = 0
for key in data_dict:
    combinations_list = generate_combinations(len(data_dict[key])-1, len(data_dict[key])-1, type=1)
    for combination in combinations_list:
        # Corectly initialize based on the first operator:
        if len(combination) == 1:
            ans = data_dict[key][0]
            for d in data_dict[key][1:]:
                if combination == '|':
                    ans = int(str(ans)+str(d))
                else:
                    ans = operations[combination](ans,d)
        else:
            ans = data_dict[key][0]
            for d,c in zip(data_dict[key][1:],combination):
                if c == '|':
                    ans = int(str(ans)+str(d))
                else:
                    ans = operations[c](ans,d)
        if ans == key:
            res2 += key
            break
print(f'Part Two = {res2}')
