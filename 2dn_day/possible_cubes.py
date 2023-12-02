# First, we need to process the input heavily
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

# This is for consistency with the values placement within the internal structure
color_codes = {'red': 0,
               'green': 1,
               'blue': 2}

data_structure = {}


for index, line in enumerate(lines):
    # Gamer are numbered consecutevely, otherwise we'll need to take the header and extract the number
    _, body = line.split(':')
    draws = body.split(';')
    sampled_values = []
    for draw in draws:
        values = [0, 0, 0]
        for segment in draw.split(','):
            value, color = segment.strip().split(' ')
            values[color_codes[color]] = int(value)
        sampled_values.append(values)
    data_structure[index+1] = sampled_values

# Now we just need to iterate over the structure and check
id_sum = 0
for game, draws in data_structure.items():
    flag = True
    for draw in draws:
        if draw[0] > 12 or draw[1] > 13 or draw[2] > 14:
            flag = False
    if flag:
        id_sum += game

print(id_sum)
