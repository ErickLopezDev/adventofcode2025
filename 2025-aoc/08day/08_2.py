def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def main():
    file_path = '08.txt'
    try:
        with open(file_path, 'r') as file:
            lines = file.read().strip().splitlines()
        points = []
        for line in lines:
            x, y, z = map(int, line.split(','))
            points.append((x, y, z))
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2 + (points[i][2] - points[j][2])**2
                edges.append((dist, i, j))
        edges.sort()
        parent = list(range(n))
        rank = [0] * n
        last_edge = None
        for dist, i, j in edges:
            if find(parent, i) != find(parent, j):
                union(parent, rank, i, j)
                last_edge = (i, j)
        if last_edge:
            x1, _, _ = points[last_edge[0]]
            x2, _, _ = points[last_edge[1]]
            print(x1 * x2)
        else:
            print("All points already connected")
    except FileNotFoundError:
        print(f"Error: file {file_path} was not found.")

if __name__ == "__main__":
    main()
