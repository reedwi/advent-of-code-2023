from collections import defaultdict

with open('20/20.txt', 'r') as file:
    data = file.read().strip()

vals = {}
for row in data.split('\n'):
    in_mod, out_mods = row.split(' -> ')
    out_mods = out_mods.split(', ')
    
    if in_mod == 'broadcaster':
        mod_type = None
    else:
        mod_type = in_mod[0]
        in_mod = in_mod[1:]
    vals[in_mod] = (mod_type, out_mods)


def part_one():
    
    num_low = 0
    num_high = 0
    memory = {}

    input_map = defaultdict(list)

    for node, (_, dests) in vals.items():
        for d in dests:
            input_map[d].append(node)

    for node, (mod_type, _) in vals.items():
        match mod_type:
            case None:
                continue
            case '%':
                memory[node] = False
            case '&':
                memory[node] = {d:False for d in input_map[node]}

    for _ in range(1000):
        todo = [(None, 'broadcaster', False)]

        while todo:
            new_todo = []

            for src, node, is_high_pulse in todo:
                if is_high_pulse:
                    num_high += 1
                else:
                    num_low += 1

                info = vals.get(node)
                if info is None:
                    continue

                mod_type, dests = info
                match mod_type:
                    case '%':
                        if is_high_pulse:
                            continue
                        state = memory[node]
                        memory[node] = not state
                        for d in dests:
                            new_todo.append((node, d, not state))
                        continue
                    case '&':
                        state = memory[node]
                        state[src] = is_high_pulse

                        if sum(state.values()) == len(state):
                            to_send = False
                        else:
                            to_send = True

                        for d in dests:
                            new_todo.append((node, d, to_send))
                        continue
                    case None:
                        for d in dests:
                            new_todo.append((node, d, is_high_pulse))
                        continue

            todo = new_todo

    answer = num_low * num_high

    print(answer)

def part_two():
    pass

print(part_one())