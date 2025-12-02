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
    if len(num_str) % 2 != 0:
        return False
    mid = len(num_str) // 2
    return num_str[0:mid] == num_str[mid:]

def get_invalid_sum(ranges_raw):
    ranges_clean = format_ranges(ranges_raw)
    return reduce(lambda accum, range: accum + get_range_sum(*range), ranges_clean, 0)
    

# test case 1
# test_input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
# 824824821-824824827,2121212118-2121212124'

# print(get_invalid_sum(test_input))

# puzzle input
input = get_input()
print(get_invalid_sum(input))
