with open('2/2.txt', 'r') as file:
    values = [line.strip() for line in file]

def part_one():
    digits = []
    max_red, max_blue, max_green = 12, 14, 13
    for line in values:
        game_id = line.split(':')[0].split(' ')[1]
        line = "".join(line.split())
        games = line.split(':')[1].split(';')
        possible = True
        for game in games:
            if not possible:
                continue
            game_pulls = game.split(',')
            for pull in game_pulls:
                if not possible:
                    continue
                if 'red' in pull:
                    value = pull.split('red')[0]
                    if int(value) > max_red:
                        possible = False
                elif 'blue' in pull:
                    value = pull.split('blue')[0]
                    if int(value) > max_blue:
                        possible = False
                elif 'green' in pull:
                    value = pull.split('green')[0]
                    if int(value) > max_green:
                        possible = False
        if possible:
            digits.append(int(game_id))
    return sum(digits)

def part_two():
    total_count = 0
    for line in values:
        color_map = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        line = "".join(line.split())
        games = line.split(':')[1].split(';')

        for game in games:
            game_pulls = game.split(',')
            for pull in game_pulls:
                if 'red' in pull:
                    value = int(pull.split('red')[0])
                    color_map['red'] = max(color_map['red'], value)
                elif 'blue' in pull:
                    value = int(pull.split('blue')[0])
                    color_map['blue'] = max(color_map['blue'], value)
                elif 'green' in pull:
                    value = int(pull.split('green')[0])
                    color_map['green'] = max(color_map['green'], value)
        line_value = 1
        for color in color_map:
            line_value = line_value * color_map[color]
        total_count += line_value
    return total_count

print(part_one())
print(part_two())