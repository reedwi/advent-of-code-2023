from collections import defaultdict
with open('15/15.txt', 'r') as file:
    data = file.read().strip()

vals = data.split(',')


def part_one():
    total_vals = []
    for sequence in vals:
        current_iter = 0
        for char in sequence:
            ascii_code = ord(char)
            current_iter += ascii_code
            current_iter *= 17
            current_iter = current_iter % 256
        total_vals.append(current_iter)
    
    return sum(total_vals)


def get_label(box, passed_label):
    for i, (label, lens) in enumerate(box):
        if label == passed_label:
            return i


def part_two():
    total_vals = []
    boxes = defaultdict(list)
    for sequence in vals:
        current_iter = 0
        label = ''
        for char in sequence:
            if char.isalpha():
                label += char
                ascii_code = ord(char)
                current_iter += ascii_code
                current_iter *= 17
                current_iter = current_iter % 256

        if sequence[-1] == '-':
            if current_iter not in boxes:
                continue
            idx = get_label(boxes[current_iter], label)
            if idx is not None:
                boxes[current_iter].pop(idx)

        else:
            if current_iter in boxes:
                idx = get_label(boxes[current_iter], label)
                if idx is not None:
                    boxes[current_iter][idx] = (label, int(sequence[-1]))
                else:
                    boxes[current_iter].append((label, int(sequence[-1])))
            else:
                boxes[current_iter].append((label, int(sequence[-1])))

    for box, slots in boxes.items():
        box_num = box + 1
        for i, (label, slot) in enumerate(slots, start=1):
            val = box_num * i * slot
            total_vals.append(val)
    
    return sum(total_vals)

print(part_one())
print(part_two())
