from collections import defaultdict
with open('3/3.txt', 'r') as file:
    values = [line.strip() for line in file]

def part_one():
    special_chars = set()
    for row in values:
        for val in row:
            if val.isdigit() or val == '.':
                continue
            special_chars.add(val)

    numbers_to_include = []
    row_length = len(values[0])
    column_length = len(values)
    for i, row in enumerate(values):
        j = 0
        while j < row_length:
            if row[j].isdigit():
                num_start = j
                num = ''
                while j < len(row) and row[j].isdigit():
                    num += row[j]
                    j += 1
                num_end = j - 1

                left_index = num_start-1 if num_start > 0 else num_start
                right_index = num_end+1 if num_end < row_length - 1 else num_end

                top = values[i-1][left_index:right_index+1] if i > 0 else None
                bottom = values[i+1][left_index:right_index+1] if i < column_length - 1 else None
                surrounding_chars = [row[left_index], row[right_index]]
                if top:
                    surrounding_chars.extend(top)
                if bottom:
                    surrounding_chars.extend(bottom)
                for char in special_chars:
                    if char in surrounding_chars:
                        numbers_to_include.append(int(num))
                        break
            else:
                j += 1
    return sum(numbers_to_include)

def part_two():
    final_number = 0
    row_length = len(values[0])
    column_length = len(values)
    asterisk_coordinates = defaultdict(list)

    for i, row in enumerate(values):
        j = 0
        while j < row_length:
            if row[j].isdigit():
                num_start = j
                num = ''
                while j < len(row) and row[j].isdigit():
                    num += row[j]
                    j += 1
                num_end = j - 1

                left_index = num_start-1 if num_start > 0 else num_start
                right_index = num_end+1 if num_end < row_length - 1 else num_end

                top = values[i-1][left_index:right_index+1] if i > 0 else []
                bottom = values[i+1][left_index:right_index+1] if i < column_length - 1 else []

                if row[left_index] == '*':
                    asterisk_coordinates[(i, left_index)].append(int(num))
                if row[right_index] == '*':
                    asterisk_coordinates[(i, right_index)].append(int(num))
                if '*' in top:
                    for jj, char in enumerate(top, start=left_index):
                        if char == '*':
                            asterisk_coordinates[(i-1, jj)].append(int(num))
                if '*' in bottom:
                    for jj, char in enumerate(bottom, start=left_index):
                        if char == '*':
                            asterisk_coordinates[(i+1, jj)].append(int(num))
            else:
                j += 1
    for asterisk in asterisk_coordinates:
        if len(asterisk_coordinates[asterisk]) == 2:
            final_number += (asterisk_coordinates[asterisk][0] * asterisk_coordinates[asterisk][1])
    return final_number

print(part_one())
print(part_two())