from heapq import heappop, heappush

with open('17/17.txt', 'r') as file:
    data = file.read().strip()

vals = [[int(char) for char in row] for row in data.split('\n')]

# Constants for directions
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_in_range(position, matrix):
    """
    Check if the given position is within the bounds of the matrix.
    :param position: A tuple (x, y) representing the position.
    :param matrix: 2D list representing the matrix.
    :return: True if position is within matrix bounds, else False.
    """
    x, y = position
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def calculate_minimum_cost(vals, mindist, maxdist):
    """
    Calculate the minimum cost to travel from the top-left to the bottom-right
    of the matrix `vals` with certain movement constraints.
    :param vals: 2D list of integers representing the matrix.
    :param mindist: Minimum distance constraint for a move.
    :param maxdist: Maximum distance constraint for a move.
    :return: Minimum cost of the path.
    """
    queue = [(0, 0, 0, -1)]  # Format: (cost, x, y, previous_direction)
    seen = set()
    costs = {}

    while queue:
        cost, x, y, prev_dir = heappop(queue)

        # Check if the goal is reached
        if x == len(vals) - 1 and y == len(vals[0]) - 1:
            return cost

        if (x, y, prev_dir) in seen:
            continue

        seen.add((x, y, prev_dir))

        for direction in range(4):
            if direction == prev_dir or (direction + 2) % 4 == prev_dir:
                continue  # Skip the backward and same direction

            cost_increase = 0
            for distance in range(1, maxdist + 1):
                xx, yy = x + DIRS[direction][0] * distance, y + DIRS[direction][1] * distance

                if not is_in_range((xx, yy), vals):
                    break

                cost_increase += vals[xx][yy]
                if distance < mindist:
                    continue

                new_cost = cost + cost_increase
                if costs.get((xx, yy, direction), float('inf')) <= new_cost:
                    continue

                costs[(xx, yy, direction)] = new_cost
                heappush(queue, (new_cost, xx, yy, direction))

    return float('inf')  # Return a large number if no path is found

part_one = calculate_minimum_cost(vals, 1, 3)
part_two = calculate_minimum_cost(vals, 4, 10)
print(part_one)
print(part_two)