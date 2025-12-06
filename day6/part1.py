import re

def format_input(filepath):
  with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read().strip()

  return [[int(string) if re.fullmatch(r'\d+', string) else string
                       for string in line.split()]
                       for line in data.split('\n')]

def hw_sum(problems):
  total = 0

  for col in range(len(problems[0])):
    answer = problems[0][col]

    for row in range(1, len(problems)-1):
      if problems[-1][col] == '*':
        answer *= problems[row][col]
      else:
        answer += problems[row][col]

    total += answer

  return total

# test case
# test_input = format_input('./test_input.txt')
# print(hw_sum(test_input))

#real input
real_input = format_input('./input.txt')
print(hw_sum(real_input))
