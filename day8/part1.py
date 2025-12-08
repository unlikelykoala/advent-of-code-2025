import functools
import math

def format_input(filepath):
    data = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            coords = [int(num) for num in line.rstrip().split(',')]
            data.append(tuple(coords))

    return data

def get_distance(point1, point2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(point1, point2)))

def create_pairs_list(boxes):
    box_len = len(boxes)
    pairs = []
    for idx1 in range(box_len):
        for idx2 in range(idx1 + 1, box_len):
            box1 = boxes[idx1]
            box2 = boxes[idx2]
            dist = get_distance(box1, box2)
            pair = (box1, box2, dist)
            pairs.append(pair)

    pairs.sort(key=lambda x: x[2])
    return pairs

def add_to_adj_list(point1, point2, adj_list):
    if point1 not in adj_list:
        adj_list[point1] = []
    adj_list[point1].append(point2)

    if point2 not in adj_list:
        adj_list[point2] = []
    adj_list[point2].append(point1)

def create_adj_list(pairs, n):
    adj_list = {}

    for i in range(n):
        point1, point2, _ = pairs[i]
        add_to_adj_list(point1, point2, adj_list)
    
    return adj_list

def get_3_biggest_circuits(adj_list):
    def traverse(point):
        if point in seen:
            return 0
        
        seen.add(point)
        box_count = 1
        for neighbor in adj_list[point]:
            box_count += traverse(neighbor)
        return box_count
        
    all_sizes = [0, 0, 0]
    seen = set()
    for key in adj_list.keys():
        box_count = traverse(key)
        all_sizes.append(box_count)

    big3 = sorted(all_sizes, reverse=True)[:3]
    return big3

def get_circuits_product(boxes, n):
    pairs = create_pairs_list(boxes)
    adj_list = create_adj_list(pairs, n)
    big3 = get_3_biggest_circuits(adj_list)
    return functools.reduce(lambda accum, next: accum * next, big3)

# test data
# test_input = format_input('./test_input.txt')
# print(get_circuits_product(test_input, 10))

# real data
real_input = format_input('./input.txt')
print(get_circuits_product(real_input, 1000))
