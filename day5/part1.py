def format_input():
  formatted_ranges = []
  formatted_ids = []

  with open('input.txt', 'r', encoding='utf-8') as f:
    location = formatted_ranges
    for line in f:
      if line == '\n':
        location = formatted_ids

      line = line.replace('\n', '')

      if location == formatted_ranges:
        startStr, endStr = line.split('-')
        range = (int(startStr), int(endStr))
        location.append(range)
      elif line:
        location.append(int(line))

  return formatted_ranges, formatted_ids

def count_fresh_items(fresh_ranges, ids):
  sorted_ranges = sorted(fresh_ranges)
  sorted_ids = sorted(ids)

  fresh_count = 0

  a = 0
  range_len = len(fresh_ranges)

  for r in range(len(ids)):
    while a < range_len and sorted_ids[r] > sorted_ranges[a][1]:
      a += 1

    if a >= range_len:
      break
    elif sorted_ranges[a][0] <= sorted_ids[r] <= sorted_ranges[a][1]:
      fresh_count += 1

  return fresh_count

# test case
test_ranges = [
  (3, 5),
  (10, 14),
  (16, 20),
  (12, 18),
]
test_ids = [1, 5, 8, 11, 17, 32]
# print(count_fresh_items(test_ranges, test_ids))

# real input
real_ranges, real_ids = format_input()
print(count_fresh_items(real_ranges, real_ids))
