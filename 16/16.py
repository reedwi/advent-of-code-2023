from collections import deque
with open('16/16.txt', 'r') as file:
    data = file.read().strip()

vals = data.split('\n')
print(vals)


def part_one():
    n,m = len(vals), len(vals[0])
    seen = set()
    q = deque([(0, -1, 0, 1)])
    while q:
        i, j, di, dj = q.pop()
        ii, jj = i + di, j + dj
        if (ii, jj, di, dj) in seen: 
            continue
        if not (0 <= ii < m and 0 <= jj < n): 
            continue
        
        seen.add((ii, jj, di, dj))
        tile = vals[ii][jj]
        match tile:
            case "/":
                di, dj = -dj, -di
            case "\\":
                di, dj = dj, di
            case "|":
                if dj:
                    di, dj = 1, 0
                    q.append((ii, jj, -1, 0))
            case "-":
                if di:
                    di, dj = 0, 1
                    q.append((ii, jj, 0, -1))
        q.append((ii, jj, di, dj))
    energized = {x[:2] for x in seen}
    return len(energized)

def get_coverage(vals, start):
    n,m = len(vals), len(vals[0])
    seen = set()
    q = deque([start])
    while q:
        i, j, di, dj = q.pop()
        ii, jj = i + di, j + dj
        if (ii, jj, di, dj) in seen: 
            continue
        if not (0 <= ii < m and 0 <= jj < n): 
            continue
        
        seen.add((ii, jj, di, dj))
        tile = vals[ii][jj]
        match tile:
            case "/":
                di, dj = -dj, -di
            case "\\":
                di, dj = dj, di
            case "|":
                if dj:
                    di, dj = 1, 0
                    q.append((ii, jj, -1, 0))
            case "-":
                if di:
                    di, dj = 0, 1
                    q.append((ii, jj, 0, -1))
        q.append((ii, jj, di, dj))
    energized = {x[:2] for x in seen}
    return len(energized)

def part_two():
    n,m = len(vals), len(vals[0])
    max_energized = 0
    for i in range(m):
        max_energized = max(max_energized, get_coverage(vals, (i, -1, 0, 1)))
        max_energized = max(max_energized, get_coverage(vals, (i, n, 0, -1)))
    for j in range(n):
        max_energized = max(max_energized, get_coverage(vals, (-1, j, 1, 0)))
        max_energized = max(max_energized, get_coverage(vals, (m, j, -1, 0)))
    
    return max_energized

print(part_one())
print(part_two())
