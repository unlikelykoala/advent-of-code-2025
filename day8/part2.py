def format_input(filepath):
    data = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            coords = [int(num) for num in line.rstrip().split(',')]
            data.append(tuple(coords))

    return data

def get_distance(point1, point2):
    return sum((a - b)**2 for a, b in zip(point1, point2))

def create_pairs_list(nodes):
    box_len = len(nodes)
    edges = []
    for idx1 in range(box_len):
        for idx2 in range(idx1 + 1, box_len):
            edge = (idx1, idx2)
            edges.append(edge)

    edges.sort(key=lambda x: get_distance(nodes[x[0]], nodes[x[1]]))
    return edges

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1
            return True
        return False

def to_wall(nodes, edge):
    idx1, idx2 = edge
    x1 = nodes[idx1][0]
    x2 = nodes[idx2][0]
    return x1 * x2

def get_distance_to_wall(nodes):
    total_nodes = len(nodes)
    edges = create_pairs_list(nodes)
    dsu = DSU(total_nodes)
    circuits = total_nodes
    for idx1, idx2 in edges:
        merged = dsu.union(idx1, idx2)
        if merged:
            circuits -= 1
        if circuits <= 1:
            return to_wall(nodes, (idx1, idx2))

# test data
test_input = format_input('./test_input.txt')
print(get_distance_to_wall(test_input))

# real data
real_input = format_input('./input.txt')
print(get_distance_to_wall(real_input))
