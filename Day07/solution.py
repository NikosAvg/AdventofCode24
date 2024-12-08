from itertools import product, combinations
import operator

# Initialize an empty dictionary
data_dict = {}

operations = {
    '+': operator.add,
    '*': operator.mul,
    '|': lambda x, y: int(f"{x}{y}"),
}
def generate_combinations(length, num_operators, operators):
    operator_combinations = []
    for pos_tuple in combinations(range(length), num_operators):  # Choose positions for operators
        for operator_tuple in product(operators, repeat=num_operators):  # All combinations of operators
            combo = [''] * length  # Initialize empty slots
            for idx, pos in enumerate(pos_tuple):
                combo[pos] = operator_tuple[idx]
            operator_combinations.append(combo)
    return operator_combinations

def calculate_result(data_dict, operators):
    res = 0
    for key, values in data_dict.items():
        num_elements = len(values) - 1
        combinations_list = generate_combinations(num_elements, num_elements, operators)
        for combination in combinations_list:
            ans = values[0]
            for d, c in zip(values[1:], combination):
                if c:  # Only apply non-empty operators
                    ans = operations[c](ans, d)
            if ans == key:
                res += key
                break
    return res

# Read Input and Initialize an empty dictionary
data_dict = {}
with open('input.txt', 'r') as file:
    for line in file:
        key, value = line.split(':')
        data_dict[int(key.strip())] = list(map(int, value.strip().split()))

# Part One: Operators are ['+', '*']
res = calculate_result(data_dict, ['+', '*'])
print(f"Part One = {res}")

# Part Two: Operators include ['+', '*', '|']
res2 = calculate_result(data_dict, ['+', '*', '|'])
print(f"Part Two = {res2}")
