with open('24/24.txt', 'r') as file:
    data = file.read().strip()

rows = [row for row in data.split('\n')]

parsed_rows = []
for line in rows:
    position_str, velocity_str = line.split(' @ ')
    position = list(map(int, position_str.split(', ')))
    velocity = list(map(int, velocity_str.split(', ')))
    parsed_rows.append((position, velocity))

def calculate_intersection(point_a, vel_a, point_b, vel_b):
    """Calculate the intersection point of two objects given their positions and velocities."""
    try:
        u = ((point_b[1] - point_a[1]) * vel_b[0] - (point_b[0] - point_a[0]) * vel_b[1]) / (vel_b[0] * vel_a[1] - vel_b[1] * vel_a[0])
        v = ((point_b[1] - point_a[1]) * vel_a[0] - (point_b[0] - point_a[0]) * vel_a[1]) / (vel_b[0] * vel_a[1] - vel_b[1] * vel_a[0])
        return u, v
    except ZeroDivisionError:
        return None, None

def part_one(parsed_rows):
    """Calculate the number of intersections within a specific range."""
    answer = 0
    for i in range(len(parsed_rows)):
        for j in range(i+1, len(parsed_rows)):
            position_a, velocity_a = parsed_rows[i]
            position_b, velocity_b = parsed_rows[j]

            u, v = calculate_intersection(position_a, velocity_a, position_b, velocity_b)
            if u is None or v is None or u < 0 or v < 0:
                continue

            intersection_x = position_b[0] + velocity_b[0] * v
            intersection_y = position_b[1] + velocity_b[1] * v
            if 200000000000000 <= intersection_x <= 400000000000000 and \
               200000000000000 <= intersection_y <= 400000000000000:
                answer += 1
    return answer

print(part_one(parsed_rows))

