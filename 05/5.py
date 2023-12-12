
with open('5/5-sample.txt', 'r') as file:
    data = file.read().strip()

parts = data.split("\n\n")
seeds, *maps = parts
seeds = [int(seed) for seed in seeds.split(':')[1].split() ]
print(seeds)


def part_one():
    vals = [seed for seed in seeds]
    for i in range(len(seeds)):
        for m in maps:
            mappings = [list(map(int, mapping.split())) for mapping in m.split('\n')[1:]]
            for dest, source, n in mappings:
                if source <= vals[i] < (source + n):
                    vals[i] = dest + (vals[i] - source)
                    break  # Break from the inner loop after the first match
                    # At first, I did not catch detail about their only being one match, I thought it should go through everything

    return min(vals)

def part_two():
    lower_bound = seeds[::2]
    upper_bound = seeds[1::2]
    seed_ranges = [(lower, lower + upper - 1) for lower, upper in zip(lower_bound, upper_bound)]  # Create (start, end) pairs for ranges
    
    final_locations = []

    for seed_range in seed_ranges:
        current_ranges = [seed_range]
        transformed_ranges = []

        for m in maps:
            mappings = [list(map(int, mapping.split())) for mapping in m.split('\n')[1:]]
            while current_ranges:
                current_range = current_ranges.pop()
                for dest, source, n in mappings:
                    source_end = source + n - 1  # End is inclusive
                    destination_end = dest + n - 1

                    # Handle various types of range overlaps
                    if current_range[1] < source or source_end < current_range[0]:  # No overlap
                        continue
                    elif source <= current_range[0] <= current_range[1] <= source_end:  # Complete overlap within source range
                        offset = current_range[0] - source
                        transformed_ranges.append((dest + offset, dest + offset + current_range[1] - current_range[0]))
                        break
                    elif current_range[0] <= source <= current_range[1] <= source_end:  # Partial overlap on right
                        offset = current_range[1] - source
                        transformed_ranges.append((dest, dest + offset))
                        current_ranges.append((current_range[0], source - 1))
                        break
                    elif source <= current_range[0] <= source_end <= current_range[1]:  # Partial overlap on left
                        offset = current_range[0] - source
                        transformed_ranges.append((dest + offset, destination_end))
                        current_ranges.append((source_end + 1, current_range[1]))
                        break
                    elif current_range[0] <= source and source_end <= current_range[1]:  # Current range envelops source range
                        transformed_ranges.append((dest, destination_end))
                        current_ranges.append((current_range[0], source - 1))
                        current_ranges.append((source_end + 1, current_range[1]))
                        break
                else:  # Current range doesn't match any source range, keep it as is
                    transformed_ranges.append(current_range)
            current_ranges = transformed_ranges
            transformed_ranges = []
        final_locations.extend(current_ranges)

    # Find the minimum location value
    return min(location[0] for location in final_locations)



print(part_one())
print(part_two())