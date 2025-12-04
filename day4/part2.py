import copy

def format_input():
    formatted_input = []

    with open('./input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            formatted_input.append(line[:-1] if line[-1] == '\n' else line)

    return formatted_input

def in_range(row, col, rows, cols):
    return (0 <= row < rows) and (0 <= col < cols)

def is_accessible(row, col, floor, rows, cols, next_floor):
    rolls = 0

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if in_range(r, c, rows, cols):
                symbol = floor[r][c]
                if symbol == '@'  and (r != row or c != col):
                    rolls += 1

    if rolls < 4:
        next_floor[row][col] = 'X'
        return True
    return False

def count_accessible_rolls(floor, next_floor):
    rolls = 0
    rows = len(floor)
    cols = len(floor[0])
    for row in range(rows):
        for col in range(cols):
            if floor[row][col] == '@' and is_accessible(row, col, floor, rows, cols, next_floor):
                rolls += 1
    return rolls

def move_and_count_rolls(floor):
    rolls = 0
    next_floor = [list(line) for line in floor]

    moved_rolls = count_accessible_rolls(floor, next_floor)

    while moved_rolls > 0:
        rolls += moved_rolls
        moved_rolls = count_accessible_rolls(copy.deepcopy(next_floor), next_floor)

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

# print(move_and_count_rolls(test_input))

# real input
real_input = format_input()
print(move_and_count_rolls(real_input))
