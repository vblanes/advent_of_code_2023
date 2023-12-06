with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

N_ROWS = len(lines)
N_COLS = len(lines[0])
print(f'Rows: {N_ROWS} - Cols: {N_COLS}')

def is_special_character(character: str):
    return (character != '.') and (not character.isdigit())


def has_special_char_around(row: int, col: int, mat: list):
    found = False
    # The order is counter-clock wise
    # superior left corner
    if row > 0 and col > 0:
        found = found or is_special_character(mat[row-1][col-1])
    # left
    if col > 0:
        found = found or is_special_character(mat[row][col-1])
    # inferior left corner
    if col > 0 and row < N_ROWS-1:
        found = found or is_special_character(mat[row+1][col-1])
    # bottom
    if row < N_ROWS-1:
        found = found or is_special_character(mat[row+1][col])
    # inferior right corner
    if row < N_ROWS-1 and col < N_COLS-1:
        found = found or is_special_character(mat[row+1][col+1])
    # right
    if col < N_COLS-1:
        found = found or is_special_character(mat[row][col+1])
    # superior right corner
    if row > 0 and col < N_COLS-1:
        found = found or is_special_character(mat[row-1][col+1])
    # top
    if row > 0:
        found = found or is_special_character(mat[row - 1][col])
    return found

acum = []
# I think we can do all checks on the way instead of creating maps
for i, line in enumerate(lines):
    parsing_number = ''
    adding_number = False
    for j, char in enumerate(line):
        # if digit, parse the number
        if char.isdigit():
            parsing_number += char
            if has_special_char_around(i, j, lines):
                adding_number = True

        else:
            if parsing_number:
                numb = int(parsing_number)
                parsing_number = ''
                if adding_number:
                    acum.append(numb)
                    adding_number = False
    # Number left to add at the end of the line
    if parsing_number and adding_number:
        acum.append(int(parsing_number))

print(sum(acum))