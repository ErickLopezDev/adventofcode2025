#!/usr/bin/python3
from collections import defaultdict

fname = "12.txt"

with open(fname) as handle:
    data = handle.read()

blocks = data.strip().split('\n\n')
items = blocks[:-1]
zones = blocks[-1]

area_map = {}
for item in items:
    ln = item.splitlines()
    idx = int(ln[0][:-1])
    grid = [list(r) for r in ln[1:]]
    filled = sum(ch == '#' for row in grid for ch in row)
    area_map[idx] = filled

count = 0
for z in zones.splitlines():
    size_spec, nums = z.split(':')
    rows, cols = map(int, size_spec.split('x'))
    nums = [int(x) for x in nums.split()]
    total_items = sum(n * area_map[i] for i, n in enumerate(nums))
    total_cells = rows * cols

    if total_items * 1.3 < total_cells:
        count += 1
    elif total_items > total_cells:
        pass
    else:
        print(f'hard total_cells={total_cells} total_items={total_items}')

print(count)
