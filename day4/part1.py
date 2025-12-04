def format_input():
    formatted_input = []

    with open('./input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            formatted_input.append(line[:-1] if line[-1] == '\n' else line)

    return formatted_input

def in_range(row, col, rows, cols):
    return (0 <= row < rows) and (0 <= col < cols)

def is_accessible(row, col, floor, rows, cols):
    rolls = 0

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if in_range(r, c, rows, cols):
                symbol = floor[r][c]
                if symbol == '@'  and (r != row or c != col):
                    rolls += 1

    return rolls < 4

def count_accessible_rolls(floor):
    rolls = 0
    rows = len(floor)
    cols = len(floor[0])
    for row in range(rows):
        for col in range(cols):
            if floor[row][col] == '@' and is_accessible(row, col, floor, rows, cols):
                rolls += 1
    return rolls

# test input
# test_input = [
#     '..@@.@@@@.',
#     '@@@.@.@.@@',
#     '@@@@@.@.@@',
#     '@.@@@@..@.',
#     '@@.@@@@.@@',
#     '.@@@@@@@.@',
#     '.@.@.@.@@@',
#     '@.@@@.@@@@',
#     '.@@@@@@@@.',
#     '@.@.@@@.@.',
# ]

# print(count_accessible_rolls(test_input))

# real input
real_input = format_input()
print(count_accessible_rolls(real_input))
