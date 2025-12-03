def format_input():
    formatted_input = []

    with open('./input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            formatted_input.append(line.replace('\n', ''))

    return formatted_input

def get_bank_joltage(bank):
    max_j = 0
    a = 0
    for r in range(1, len(bank)):
        j = int(bank[a] + bank[r])
        max_j = max([j, max_j])
        if bank[a] < bank[r]:
            a = r
    return max_j

def get_total_joltage(banks):
    result = 0
    for bank in banks:
        j = get_bank_joltage(bank)
        result += j
    return result

# test case
test_input = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
# print(get_total_joltage(test_input))

# real input
real_input = format_input()
print(get_total_joltage(real_input))
