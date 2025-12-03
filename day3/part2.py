def format_input():
    formatted_input = []

    with open('./input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            formatted_input.append(line.replace('\n', ''))

    return formatted_input

def get_bank_joltage(bank):
    length = len(bank)
    j = 0
    exp = 11
    stop = -1
    for start in range(length-12, length):
        a = start
        # print('a', a, bank[a])
        for r in range(a - 1, stop, -1):
            # print('r', r, bank[r])
            if bank[a] <= bank[r]:
                a = r
        j += int(bank[a]) * 10**exp
        exp -= 1
        stop = a
        # print('final a', a, bank[a])
    return j

def get_total_joltage(banks):
    result = 0
    for bank in banks:
        j = get_bank_joltage(bank)
        result += j
    return result

# test case
# test_input = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
# print(get_total_joltage(test_input) == 3121910778619)
# print(get_bank_joltage('818181911112111'))

# real input
real_input = format_input()
print(get_total_joltage(real_input))
