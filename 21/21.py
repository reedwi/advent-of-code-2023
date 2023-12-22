from collections import deque
with open('21/21.txt', 'r') as file:
    data = file.read().strip()

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

vals = [row for row in data.split('\n')]


def part_one():
    for i, row in enumerate(vals):
        if 'S' not in row:
            continue
        start_loc = row.find('S')
        starting_point = (start_loc, i)

    visited = {}
    last_positions = deque()
    last_positions.append(starting_point)
    x_range = len(vals[0])
    y_range = len(vals)
    for i in range(64):
        next_positions = deque()
        while last_positions:
            point = last_positions.pop()
            if point in visited:
                continue
            visited[point] = i

            for d in DIRS:
                x, y = point[0] + d[0], point[1] + d[1]

                if (0 <= x < x_range and 0 <= y < y_range and vals[x][y] != '#'):
                    next_positions.append((x, y))
        last_positions.extend(next_positions)
    
    for pos in last_positions:
        visited[pos] = 64

    ans = 0
    for (x,y), steps in visited.items():
        if steps % 2 == 0:
            ans += 1
    return ans

print(part_one())