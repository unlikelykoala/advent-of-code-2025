def format_input(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read().rstrip().split('\n')

    return data

def count_timelines(beam_chart):
    memo = {}
    root_col = beam_chart[0].index('S')
    start_row = 1
    last_row = len(beam_chart) - 1

    def traverse(row, col):
        if row == last_row:
            return 1
        
        key = f'{row}-{col}'
        if key in memo:
            return memo[key]

        next_row = row + 1
        if beam_chart[row][col] == '^':
            memo[key] = traverse(next_row, col-1) + traverse(next_row, col+1)
        else:
            memo[key] = traverse(next_row, col)

        return memo[key]

    return traverse(start_row, root_col)

# test case
# test_input = format_input('./test_input.txt')
# print(count_splits(test_input))

# real case
input = format_input('./input.txt')
print(count_timelines(input))
