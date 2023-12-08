from collections import Counter, defaultdict
from math import lcm

with open('8/8.txt', 'r') as file:
    data = file.read().strip()

instructions, coords = data.split('\n\n')
coords = coords.split('\n')
location_map = {}
for coord in coords:
    coord = coord.split('=')
    location = coord[0].strip()
    left = coord[1].split(',')[0].strip().replace('(', '')
    right = coord[1].split(',')[1].strip().replace(')', '')
    location_map[location] = (left, right)

# values = [(game.split()[0], game.split()[1]) for game in lines]
# possible_cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def part_one():
    AAA = 'AAA'
    ZZZ = 'ZZZ'

    current_location = AAA
    i = 0
    total_count = 0
    while i < len(instructions):
        if instructions[i] == 'L':
            current_location = location_map[current_location][0]
        else:
            current_location = location_map[current_location][1]
        if current_location == ZZZ:
            return total_count + 1

        i += 1
        total_count += 1
        if i == len(instructions):
            i = 0

def part_two():
    end_locations = [key for key in location_map if key.endswith('Z')]
    start_locations = [key for key in location_map if key.endswith('A')]  
    zzzs = []
    for start in start_locations:
        i = 0
        total_count = 0
        current_location = start
        while i < len(instructions):
            if instructions[i] == 'L':
                current_location = location_map[current_location][0]
            else:
                current_location = location_map[current_location][1]
            
            i += 1
            total_count += 1

            if current_location in end_locations:
                zzzs.append(total_count)
                break
            if i == len(instructions):
                i = 0
    return lcm(*zzzs)

print(part_one())
print(part_two())