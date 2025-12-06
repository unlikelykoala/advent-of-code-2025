import os
import functools

def format_input():
    formatted_input = []

    with open('./input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            char_list = list(line)
            formatted_input.append(char_list[:-1] if line[-1] == '\n' else char_list)

    return formatted_input

def in_range(row, col, rows, cols):
    return (0 <= row < rows) and (0 <= col < cols)

def is_accessible(row, col, floor, floor_updates, rows, cols):
    rolls = 0
    
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if in_range(r, c, rows, cols):
                symbol = floor[r][c]
                if symbol in '@X' and (r != row or c != col):
                    rolls += 1

    if rolls < 4:
        floor[row][col] = 'X'
        floor_updates.add((row, col))
        return True
    return False

def count_accessible_rolls(floor, floor_updates):
    rolls = 0
    rows = len(floor)
    cols = len(floor[0])
    for row in range(rows):
        for col in range(cols):
            if floor[row][col] == '@' and is_accessible(row, col, floor, floor_updates, rows, cols):
                rolls += 1

    for row, col in floor_updates:
        floor[row][col] = '.'
    return rolls

def move_and_count_rolls(floor):
    rolls = 0
    floor_updates = set()
    moved_rolls = count_accessible_rolls(floor, floor_updates)

    while moved_rolls > 0:
        floor_updates.clear()
        rolls += moved_rolls
        moved_rolls = count_accessible_rolls(floor, floor_updates)

    return rolls

# test input
# test_input = [
#     list('..@@.@@@@.'),
#     list('@@@.@.@.@@'),
#     list('@@@@@.@.@@'),
#     list('@.@@@@..@.'),
#     list('@@.@@@@.@@'),
#     list('.@@@@@@@.@'),
#     list('.@.@.@.@@@'),
#     list('@.@@@.@@@@'),
#     list('.@@@@@@@@.'),
#     list('@.@.@@@.@.'),
# ]

# print(move_and_count_rolls(test_input))

# real input
real_input = format_input()
print(move_and_count_rolls(real_input))
