def ints(s):
    return [int(x) for x in s.split()]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def all_pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            pairs.append((i, j))
    return pairs

def solve(points):
    rows = sorted(set(r for r, _ in points))
    cols = sorted(set(c for _, c in points))
    normalized_points = [(2*rows.index(r), 2*cols.index(c)) for r, c in points]
    height = 2*len(rows) + 1
    width = 2*len(cols) + 1
    boundaries = set(normalized_points)
    for (r1,c1),(r2,c2) in zip(normalized_points, normalized_points[1:] + [normalized_points[0]]):
        if r1 == r2:
            for c in range(min(c1,c2), max(c1,c2)+1):
                boundaries.add((r1,c))
        else:
            for r in range(min(r1,r2), max(r1,r2)+1):
                boundaries.add((r,c1))
    grid = set((r,c) for r in range(-1, height) for c in range(-1, width))
    outside = set()
    stack = [(-1,-1)]
    while stack:
        r, c = stack.pop()
        if (r,c) in outside:
            continue
        outside.add((r,c))
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if (nr,nc) in grid and (nr,nc) not in boundaries:
                stack.append((nr,nc))
    inside = grid - outside
    max_area = 0
    for i1, i2 in all_pairs(normalized_points):
        r1, c1 = normalized_points[i1]
        r2, c2 = normalized_points[i2]
        R1, R2 = min(r1,r2), max(r1,r2)
        C1, C2 = min(c1,c2), max(c1,c2)
        if all((r,c) in inside for r in range(R1,R2+1) for c in range(C1,C2+1)):
            p1, p2 = points[i1], points[i2]
            area = (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)
            max_area = max(max_area, area)
    return max_area

def main():
    with open("09.txt") as f:
        ps = [tuple(map(int, line.split(','))) for line in f.read().strip().splitlines()]
    print(solve(ps))

main()
