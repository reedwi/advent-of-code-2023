
with open('9/9.txt', 'r') as file:
    data = file.read().strip()

vals = [[int(val) for val in line.split()] for line in data.split('\n')]



def part_one():
    total_vals = []
    for line in vals:
        line_history = [line]
        while sum(line_history[-1]) != 0:
            differences = [y - x for x, y in zip(line_history[-1], line_history[-1][1:])]
            line_history.append(differences)
        
        line_history.reverse()
        len_lh = len(line_history)

        for i, difference in enumerate(line_history):
            if i == len_lh - 1:          
                break
            line_history[i+1].append(difference[-1] + line_history[i+1][-1])
        
        total_vals.append(line_history[-1][-1])
    return sum(total_vals)

def part_two():
    total_vals = []
    for line in vals:
        line_history = [line]
        while sum(line_history[-1]) != 0:
            differences = [y - x for x, y in zip(line_history[-1], line_history[-1][1:])]
            line_history.append(differences)
        
        line_history.reverse()
        len_lh = len(line_history)

        for i, difference in enumerate(line_history):
            if i == len_lh - 1:          
                break
            line_history[i+1].insert(0, line_history[i+1][0] - difference[0])
        
        total_vals.append(line_history[-1][0])
    return sum(total_vals)

print(part_one())
print(part_two())