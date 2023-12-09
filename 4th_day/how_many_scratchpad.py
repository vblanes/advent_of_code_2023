with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

card_counter = {i: 1 for i in range(len(lines))}

for i, line in enumerate(lines):
    _, body = line.split(':')
    winning_numbers, elf_numbers = body.split('|')
    multiplier = card_counter[i]
    # transform each part of the str to list of actual ints
    winning_numbers = {int(wn) for wn in winning_numbers.strip().split(' ') if wn}
    elf_numbers = {int(en) for en in elf_numbers.strip().split(' ') if en}
    intersection = elf_numbers.intersection(winning_numbers)
    # matching numbers determine the amount of cards affects, the current multiplier is added
    for s in range(i+1, i+len(intersection)+1):
        # sanity check for no copies past original cards
        if s in card_counter:
            card_counter[s] += multiplier

print(sum(card_counter.values()))