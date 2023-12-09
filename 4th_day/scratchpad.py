with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

acum = 0

for line in lines:
    header, body = line.split(':')
    winning_numbers, elf_numbers = body.split('|')
    # transform each part of the str to list of actual ints
    winning_numbers = {int(wn) for wn in winning_numbers.strip().split(' ') if wn}
    elf_numbers = {int(en) for en in elf_numbers.strip().split(' ') if en}

    intersection = elf_numbers.intersection(winning_numbers)
    if len(intersection) > 0:
        acum += 2 ** (len(intersection)-1)

print(acum)