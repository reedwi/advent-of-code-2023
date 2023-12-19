import math
from matplotlib.path import Path

with open('18/18-sample.txt', 'r') as file:
    data = file.read().strip()

vals = [row.split(' ') for row in data.split('\n')]

def part_one():
    path = [(0,0)]
    for d, depth, code in vals:
        depth = int(depth)
        last_point = path[-1]
        match d:
            case 'D':
                next_point = (last_point[0], last_point[1] + depth)
            case 'U':
                next_point = (last_point[0], last_point[1] - depth)
            case 'R':
                next_point = (last_point[0] + depth, last_point[1])
            case 'L':
                next_point = (last_point[0] - depth, last_point[1])
        path.append(next_point)
    print(path)
    length = 0
    for i in range(len(path) - 1):
        length += math.sqrt((path[i+1][0] - path[i][0])**2 + (path[i+1][1] - path[i][1])**2)

    # Get the bounding box of the polygon
    min_x = min(x for x, _ in path)
    max_x = max(x for x, _ in path)
    min_y = min(y for _, y in path)
    max_y = max(y for _, y in path)


    # Count points inside the polygon or on the boundary
    count = 0
    p_path = Path(path)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if is_point_inside_or_on_boundary((x, y), p_path):
                count += 1
    return count + length

def is_point_inside_or_on_boundary(point, polygon):
    return polygon.contains_point(point, radius=-1e-10)


def hex_to_instructions(hex_code):
    # Remove the '#' character and split the code
    hex_code = hex_code.lstrip('#')
    distance_hex = hex_code[:-1]
    direction_hex = hex_code[-1]

    # Convert the distance from hexadecimal to an integer
    distance = int(distance_hex, 16)

    # Map the direction
    directions = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    direction = directions.get(direction_hex, 'Unknown')

    return direction, distance


def shoelace(points):
  area = 0
  for (y1, x1), (y2, x2) in zip(points, points[1:] + [points[0]]):
    area += x1 * y2 - x2 * y1
  return area / 2

def area(commands):
  y, x = 0, 0
  d = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
  points = [(y, x)]
  for vdir, vlen in commands:
    dy, dx = d[vdir]
    y += dy * vlen
    x += dx * vlen
    points.append((y, x))
  return int(shoelace(points) + sum(vlen for vdir, vlen in commands) / 2 + 1)

def part_two():
    path = [(0,0)]
    pos = 0
    ans = 16
    for row in vals:
        code = row[-1].replace('(', '').replace(')', '')
        d, depth = hex_to_instructions(code)

        last_point = path[-1]
        match d:
            case 'D':
                next_point = (last_point[0], last_point[1] + depth)
                x, y = 0, depth
                n = depth
            case 'U':
                next_point = (last_point[0], last_point[1] - depth)
                x, y = 0, -depth
                n = -depth
            case 'R':
                next_point = (last_point[0] + depth, last_point[1])
                x, y = depth, 0
                n = depth
            case 'L':
                next_point = (last_point[0] - depth, last_point[1])
                x, y = -depth, 0
                n = -depth
        path.append(next_point)

        pos += x
        ans += y * pos + n/2

    return ans

print(part_one())
print(part_two())

plan = list(map(str.split, open('18/18-sample.txt')))
print(plan)
dirs = {'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1),
        '0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}

def f(steps, pos=0, ans=1):
    print(pos)
    print(ans)
    for (x,y), n in steps:
        # print(f'x: {x}, y:{y}, n:{n}')
        pos += x*n
        ans += y*n * pos + n/2

    return int(ans)

print(f((dirs[d],    int(s))          for d,s,_ in plan),
      f((dirs[c[7]], int(c[2:7], 16)) for _,_,c in plan))
