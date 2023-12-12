
with open('11/11.txt', 'r') as file:
    data = file.read().strip()


# print(len(vals))


def part_one():
    vals = [line for line in data.split('\n')]
    indexes = []
    for i, line in enumerate(vals):
        if '#' not in line:
            empty_line = line
            indexes.append(i)


    for i, idx in enumerate(indexes):
        vals.insert(i+idx, empty_line)


    vals = list(zip(*vals[::-1]))
    indexes = []
    for i, line in enumerate(vals):
        if '#' not in line:
            empty_line = line
            indexes.append(i)

    for i, idx in enumerate(indexes):
        vals.insert(i+idx, empty_line)

    vals = list(zip(*vals[::-1]))
    locations = []
    unique_pairs = set()
    for y, line in enumerate(vals):
        for x, char in enumerate(line):
            if char == '#':
                locations.append((x, y))
    
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            # Adding each pair as a frozenset to ensure that order doesn't matter
            unique_pairs.add(frozenset([locations[i], locations[j]]))

    min_distances = []
    detailed_distances = {}
    for pairs in unique_pairs:
        p1, p2 = list(pairs)
        distance = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
        min_distances.append(distance)
        detailed_distances[pairs] = {'x_distance': abs(p2[0] - p1[0]), 'y_distance': abs(p2[1] - p1[1]), 'total_distance': distance}

    return sum(min_distances)


def part_two():
    vals = [line for line in data.split('\n')]
    row_idx = []
    for i, line in enumerate(vals):
        if '#' not in line:
            row_idx.append(i)

    flipped_vals = list(zip(*vals[::-1]))
    col_idx = []
    for i, line in enumerate(flipped_vals):
        if '#' not in line:
            col_idx.append(i)


    # vals = list(zip(*vals[::-1]))
    locations = []
    unique_pairs = set()

    for y, line in enumerate(vals):
        for x, char in enumerate(line):
            if char == '#':
                locations.append((x, y))
    
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            # Adding each pair as a frozenset to ensure that order doesn't matter
            unique_pairs.add(frozenset([locations[j], locations[i]]))

    min_distances = []
    for pairs in unique_pairs:
        p1, p2 = list(pairs)
        x_distance = abs(p2[0] - p1[0])
        y_distance = abs(p2[1] - p1[1])


        rows_encountered = sum(1 for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1) if i in row_idx)
        columns_encountered = sum(1 for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1) if i in col_idx )

        x_distance = (x_distance - columns_encountered) + (columns_encountered * 1000000)
        y_distance = (y_distance - rows_encountered) + (rows_encountered * 1000000)

        # Summing horizontal and vertical distances
        distance = x_distance + y_distance

        min_distances.append(distance)

    return sum(min_distances)
print(part_one())
print(part_two())


