def format_input(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')

    return data

def count_splits(beam_chart):
    splitters = 0
    start_idx = beam_chart[0].index('S')
    curr_beams = set([start_idx])

    for r in range(1, len(beam_chart)-1):
        next_beams = set()

        for idx in curr_beams:
            if beam_chart[r][idx] == '^':
                splitters += 1
                next_beams.update([idx-1, idx+1])
            else:
                next_beams.add(idx)
        
        curr_beams = next_beams
    
    return splitters

# test case
# test_input = format_input('./test_input.txt')
# print(count_splits(test_input))

# real case
input = format_input('./input.txt')
print(count_splits(input))
