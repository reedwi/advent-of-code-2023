import re
with open('19/19.txt', 'r') as file:
    data = file.read().strip()

def ints(s):
	return list(map(int, re.findall(r'\d+', s)))

workflows, parts = data.split('\n\n')
parts = [ints(row) for row in parts.split('\n')]
workflows = {row.split("{")[0]: row.split("{")[1][:-1] for row in workflows.split("\n")}



def part_one():
    accepted = []
    for i, part in enumerate(parts):
        x, m, a, s = part
        workflow = workflows['in']
        run = True
        while run:
            for work in workflow.split(','):
                match work:
                    case 'A':
                        accepted.append(sum(part))
                        run = False
                        break
                    case 'R':
                        run = False
                        break

                if ':' not in work:
                    workflow = workflows[work]
                    break
                else:
                    condition, outcome = work.split(':')
                    if not eval(condition):
                        continue
                    match outcome:
                        case 'A':
                            accepted.append(sum(part))
                            run = False
                            break
                        case 'R':
                            run = False
                            break
                        case _:
                            workflow = workflows[outcome]
                            break
    return sum(accepted)


def part_two():
    pass

print(part_one())
print(part_two())

