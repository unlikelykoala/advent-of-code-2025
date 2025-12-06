def format_input():
  formatted_ranges = []

  with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
      if line == '\n':
        break

      line = line.replace('\n', '')
      startStr, endStr = line.split('-')
      range = (int(startStr), int(endStr))
      formatted_ranges.append(range)

  return formatted_ranges

def is_overlap(cur, next):
  return cur[1] >= next[0]

def get_new_current_range(cur, next):
  return (min([cur[0], next[0]]), max(cur[1], next[1]))

def get_range_count(cur):
  start, end = cur
  return end - start + 1

def get_fresh_id_count(fresh_ranges):
  sorted_ranges = sorted(fresh_ranges)
  total = 0
  current_range = sorted_ranges[0]

  for i in range(1, len(sorted_ranges)):
    next_range = sorted_ranges[i]
    if is_overlap(current_range, next_range):
      current_range = get_new_current_range(current_range, next_range)
    else:
      total += get_range_count(current_range)
      current_range = next_range

  total += get_range_count(current_range)
  return total

# test case
test_ranges = [
  (3, 5),
  (10, 14),
  (16, 20),
  (12, 18),
]
# print(get_fresh_id_count(test_ranges))

# real input
real_ranges = format_input()
print(get_fresh_id_count(real_ranges))
