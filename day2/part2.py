from functools import reduce

def get_input():
    with open('./input.txt', 'r') as f:
        data = f.read()
    return data

def format_range(range):
    return [int(num_str) for num_str in range.split('-')]

def format_ranges(ranges):
    return [format_range(range) for range in ranges.split(',')]

def get_range_sum(first, last):
    invalid_sum = 0
    for num in range(first, last + 1):
        if is_invalid(num):
            invalid_sum += num
    return invalid_sum

def is_invalid(num):
    num_str = str(num)
    mid_idx = len(num_str) // 2
    for stop_idx in range(1, mid_idx+1):
        sub = num_str[:stop_idx]
        if is_repeated(sub, num_str):
            return True
    return False

def is_repeated(substr, full_str):
    sub_len = len(substr)
    full_len = len(full_str)

    for start_idx in range(sub_len, full_len, sub_len):
        if substr != full_str[start_idx:start_idx+sub_len]:
            return False
        
    return True

def get_invalid_sum(ranges_raw):
    ranges_clean = format_ranges(ranges_raw)
    return reduce(lambda accum, range: accum + get_range_sum(*range), ranges_clean, 0)
    
# invalid_ids = [11, 22, 99, 111, 999, 1010, 1188511885, 222222, 446446, 38593859, 565656, 824824824, 2121212121]
# for num in invalid_ids:
#     if not is_invalid(num):
#         print(num)

# print(is_invalid(2121212118))

# test case 1
# test_input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
# 824824821-824824827,2121212118-2121212124'

# print(get_invalid_sum(test_input))

# puzzle input
input = get_input()
print(get_invalid_sum(input))

