from collections import defaultdict
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

N_ROWS = len(lines)
N_COLS = len(lines[0])
ASTERISK = '*'


def has_special_asterisk(row: int, col: int, mat: list) -> tuple:
    # The order is counter-clock wise
    # superior left corner
    if row > 0 and col > 0:
        if mat[row-1][col-1] == ASTERISK:
            return row-1, col-1
    # left
    if col > 0:
        if mat[row][col-1] == ASTERISK:
            return row, col-1
    # inferior left corner
    if col > 0 and row < N_ROWS-1:
        if mat[row+1][col-1] == ASTERISK:
            return row+1, col-1
    # bottom
    if row < N_ROWS-1:
        if mat[row+1][col] == ASTERISK:
            return row+1, col
    # inferior right corner
    if row < N_ROWS-1 and col < N_COLS-1:
        if mat[row+1][col+1] == ASTERISK:
            return row+1, col+1
    # right
    if col < N_COLS-1:
        if mat[row][col+1] == ASTERISK:
            return row, col+1
    # superior right corner
    if row > 0 and col < N_COLS-1:
        if mat[row-1][col+1] == ASTERISK:
            return row-1, col+1
    # top
    if row > 0:
        if mat[row - 1][col] == ASTERISK:
            return row-1, col


asterisk_map = defaultdict(list)
# I think we can do all checks on the way instead of creating maps
for i, line in enumerate(lines):
    parsing_number = ''
    coords = None
    for j, char in enumerate(line):
        # if digit, parse the number
        if char.isdigit():
            parsing_number += char
            if not coords:
                coords = has_special_asterisk(i, j, lines)
        else:
            if parsing_number:
                numb = int(parsing_number)
                parsing_number = ''
                if coords:
                    asterisk_map[coords].append(numb)
                    coords = None

    # Number left to add at the end of the line
    if parsing_number and coords:
        asterisk_map[coords].append(int(parsing_number))

acum = 0
for k, v in asterisk_map.items():
    if len(v) == 2:
        acum += (v[0]*v[1])

print(acum)
