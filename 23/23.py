from collections import defaultdict
with open('23/23.txt', 'r') as file:
    data = file.read().strip()

vals = [list(row) for row in data.split('\n')]

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

def part_one():
    n = len(vals)
    m = len(vals[0])

    edges = defaultdict(set)
    for r, row in enumerate(vals):
        for c, v in enumerate(row):
            if v == ".":
                for (rr, cc) in DIRS:
                    ar, ac = r + rr, c + cc
                    if not (0 <= ar < len(vals) and 0 <= ac < len(row)):
                        continue
                    if vals[ar][ac] == ".":
                        edges[(r, c)].add((ar, ac))
                        edges[(ar, ac)].add((r, c))
            if v == ">":
                edges[(r, c)].add((r, c + 1))
                edges[(r, c - 1)].add((r, c))
            if v == "v":
                edges[(r, c)].add((r + 1, c))
                edges[(r - 1, c)].add((r, c))


    q = [(0, 1, 0)]
    visited = set()
    best = 0
    while q:
        r, c, d = q.pop()
        if d == -1:
            visited.remove((r, c))
            continue
        if (r, c) == (n - 1, m - 2):
            best = max(best, d)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        q.append((r, c, -1))
        for ar, ac in edges[(r, c)]:
            q.append((ar, ac, d + 1))
    return best

print(part_one())