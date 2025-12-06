import re
from functools import reduce

def format_input(filepath):
  with open(filepath, 'r', encoding='utf-8') as f:
    data = re.sub(r'\n$', '', f.read())

  return [line for line in data.split('\n')]

def multiply(lst):
  return reduce(lambda x, y: x * y, lst)


def hw_sum2(problems):
  total = 0
  curr_num = ''
  curr_nums = []

  for col in range(len(problems[0])-1, -1, -1):
    for row in range(0, len(problems)-1):
      curr_num += problems[row][col].replace(' ', '')

    if curr_num:
        curr_nums.append(int(curr_num))
    curr_num = ''

    op = problems[-1][col]

    if op == '*':
      answer = multiply(curr_nums)
      curr_nums = []
      total += answer
    elif op == '+':
      answer = sum(curr_nums)
      curr_nums = []
      total += answer

  return total

# test case
# test_input = format_input('./test_input.txt')
# print(hw_sum2(test_input))

#real input
real_input = format_input('./input.txt')
print(hw_sum2(real_input))
