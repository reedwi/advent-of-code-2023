from matplotlib.path import Path

with open('10/10.txt', 'r') as file:
    data = file.read().strip()

vals = [[char for char in line] for line in data.split('\n')]

for i, line in enumerate(vals):
    for j, char in enumerate(line):
        if char == 'S':
            starting_point = (i, j)

pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

def part_one():
    encountered_places = dict()

    search_queue = [(starting_point, 0)]
    while len(search_queue) > 0:
        current, distance = search_queue.pop(0)
        if current in encountered_places:
            continue
        encountered_places[current] = distance
        i, j = current
        available_directions = pipe_types[vals[i][j]]
        for direction in available_directions:
            di, dj, opposite = directions[direction]
            new = (i + di, j + dj)
            if i + di < 0 or i + di >= len(vals):
                continue
            if j + dj < 0 or j + dj >= len(vals[i + di]):
                continue
            target = vals[i + di][j + dj]
            if target not in pipe_types:
                continue
            target_directions = pipe_types[target]
            if opposite in target_directions:
                search_queue.append((new, distance + 1))

    return max(encountered_places.values())


def part_two():
    encountered_places = dict()

    search_queue = [(starting_point, 0)]
    while len(search_queue) > 0:
        current, distance = search_queue.pop(0)
        if current in encountered_places:
            continue
        encountered_places[current] = distance
        i, j = current
        available_directions = pipe_types[vals[i][j]]
        for direction in available_directions:
            di, dj, opposite = directions[direction]
            new = (i + di, j + dj)
            if i + di < 0 or i + di >= len(vals):
                continue
            if j + dj < 0 or j + dj >= len(vals[i + di]):
                continue
            target = vals[i + di][j + dj]
            if target not in pipe_types:
                continue
            target_directions = pipe_types[target]
            if opposite in target_directions:
                search_queue.append((new, distance + 1))
    total = 0
    for i in range(len(vals)):
        in_ = False
        for j in range(len(vals[0])):
            if (i, j) in encountered_places:
                if vals[i][j] in "|JL" or (vals[i][j]=="S"):
                    in_ = not in_
            else:
                total += in_
    return total

print(part_one())
print(part_two())


