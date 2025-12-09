def format_input(filepath):
  data = []

  with open(filepath, 'r', encoding='utf-8') as f:
    for line in f:
      data.append(tuple(int(num) for num in line.rstrip().split(',')))
  
  return data

def largest_rectangle(red_tiles):
  length = len(red_tiles)
  largest = 0
  for idx1 in range(length):
    for idx2 in range(idx1+1, length):
      col1, row1 = red_tiles[idx1]
      col2, row2 = red_tiles[idx2]
      area = (abs(col2 - col1) + 1) * (abs(row2 - row1) + 1)
      largest = max([largest, area])

  return largest

# test case
# test_input = format_input('./test_input.txt')
# print(largest_rectangle(test_input))

# real case
real_input = format_input('./input.txt')
print(largest_rectangle(real_input))
