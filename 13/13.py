with open('13/13.txt', 'r') as file:
    data = file.read().strip()

vals = [group.split('\n') for group in data.split('\n\n')]

def reflect_check(group):
    row_len = len(group)
    reflects = []
    for i, row in enumerate(group):
        if i == 0 or row != group[i-1]:
            continue
        reflect = True
        j = 1

        while i+j <= row_len - 1 and i-1-j >= 0 and reflect:
            if group[i + j] == group[i - 1 - j]:
                j += 1
                continue
            else:
                reflect = False
        if reflect:
            reflects.append([i, j])
    return reflects

def is_one_char_diff(str1, str2):
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    return True

def reflect_check_smudge(group, skip=None):
    row_len = len(group)
    reflects = []
    for i, row in enumerate(group):
        if i == 0 or i == skip:
            continue

        smudged = False
        char_diff = is_one_char_diff(row, group[i-1])
        if row != group[i-1] and char_diff is False:
            continue

        if row != group[i-1]:
            smudged = True
        
        reflect = True
        j = 1
        while i+j <= row_len - 1 and i-1-j >= 0 and reflect:
            if group[i + j] == group[i - 1 - j]:
                j += 1
                continue
            elif smudged is False and is_one_char_diff(group[i + j], group[i - 1 - j]):
                j += 1
                smudged = True
                continue
            else:
                reflect = False
        if reflect:
            reflects.append([i, j])
    return reflects

def part_one():
    reflections = []
    for _, group in enumerate(vals):

        rows = reflect_check(group)  
        rotated_group = [''.join(row[i] for row in group) for i in range(len(group[0]))]
        cols = reflect_check(rotated_group)

        if rows:
            val = rows[0][0] * 100
        else:
            val = cols[0][0]
        reflections.append(val)

    return sum(reflections)

def part_two():
    reflections = []
    for _, group in enumerate(vals):

        rows = reflect_check(group)
        rotated_group = [''.join(row[i] for row in group) for i in range(len(group[0]))]
        cols = reflect_check(rotated_group)

        if rows:
            row_val, col_val = rows[0][0], None
        else:
            col_val, row_val = cols[0][0], None
        
        rows_smudge = reflect_check_smudge(group=group, skip=row_val)
        cols_smudge = reflect_check_smudge(rotated_group, skip=col_val)

        if rows_smudge:
            val = rows_smudge[0][0] * 100
        elif cols_smudge:
            val = cols_smudge[0][0]

        reflections.append(val)
    return sum(reflections)


print(part_one())
print(part_two())
