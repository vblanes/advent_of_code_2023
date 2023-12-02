with open ('input.txt', 'r') as file:
    lines = file.read().split()

val = 0

for line in lines:

    for char in line:
        if char.isdigit():
            front_digit = char
            break

    for char in line[::-1]:
        if char.isdigit():
            back_digit = char
            break

    val += int(f'{front_digit}{back_digit}')

print(val)
