from collections import Counter

file_path = '08.txt'

def generate_pairs(points):
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            euc = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            edges.append((euc, i, j))
    return edges

def get_root(x, parent):
    if parent[x] != x:
        parent[x] = get_root(parent[x], parent)
    return parent[x]

def merge(x, y, size, parent):
    x_root = get_root(x, parent)
    y_root = get_root(y, parent)
    if x_root == y_root:
        return False
    if size[x_root] < size[y_root]:
        x_root, y_root = y_root, x_root
    parent[y_root] = x_root
    size[x_root] += size[y_root]
    return True

def main():
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        points = [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]
        edges = generate_pairs(points)
        edges.sort()
        n = len(points)
        parent = list(range(n))
        size = [1] * n
        num_connections = min(1000, len(edges))
        for idx in range(num_connections):
            _, i, j = edges[idx]
            merge(i, j, size, parent)
        for k in range(n):
            get_root(k, parent)

        circuit_count = Counter(get_root(k, parent) for k in range(n))
        largest_sizes = sorted(circuit_count.values(), reverse=True)

        result = 1
        for s in largest_sizes[:3]:
            result *= s

        print(f"result: {result}")

    except FileNotFoundError:
        print(f"Error: file {file_path} was not found.")

main()
