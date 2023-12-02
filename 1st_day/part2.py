with open ('input.txt', 'r') as file:
    lines = file.read().split()

val = 0

spelled = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for line in lines:
    numeric_values = []
    for index, char in enumerate(line):
        if char.isdigit():
            numeric_values.append(char)

        # shortcut a lot of tests
        if char not in {'o', 't', 'f', 's', 'e', 'n'}:
            continue

        for spelled_numbers in spelled:
            # find is just like 'index' method but from one index to the end of the str
            # that's why if we are iterating over the line, we can get multiples occurrences of the same word
            if line.find(spelled_numbers, index) == index:
                numeric_values.append(spelled[spelled_numbers])
                continue

    # here I should have all numeric values
    val += int(f'{numeric_values[0]}{numeric_values[-1]}')
print(val)