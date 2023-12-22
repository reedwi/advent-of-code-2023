from collections import defaultdict
import itertools as it
with open('22/22.txt', 'r') as file:
    data = file.read().strip()

bricks = []
for line in data.split('\n'):
    a, b = line.rstrip().split("~")
    bricks.append([list(map(int, a.split(","))), list(map(int, b.split(",")))])

def fall(bricks):
    bricks.sort(key=lambda ps: min(ps[0][2], ps[1][2]))

    height = defaultdict(lambda:(0,-1))
    pos = []
    for i, (a, b) in enumerate(bricks):
        xs = range(min(a[0], b[0]), max(a[0], b[0]) + 1)
        ys = range(min(a[1], b[1]), max(a[1], b[1]) + 1)
        h = max(a[2], b[2]) - min(a[2], a[2]) + 1
        base = 0
        for x, y in it.product(xs, ys):
            p = (x, y)
            if p not in height:
                continue
            z, _ = height[p]
            base = max(base, z)

        deps = set()
        for x, y in it.product(xs, ys):
            p = (x, y)
            if p not in height:
                continue
            z, owner = height[p]
            if z == base:
                deps.add(owner)

        pos.append((base, deps))
        for x, y in it.product(xs, ys):
            height[(x, y)] = (base + h, i)

    depend = [dep for _, dep in pos]
    support = [set[int]() for _ in pos]
    for i, dep in enumerate(depend):
        for d in dep:
            support[d].add(i)

    return depend, support


def part_one():
    depend, _ = fall(bricks)
    safe = {*range(len(depend))}
    for deps in depend:
        if len(deps) == 1:
            safe -= deps
    return len(safe)

def part_two():
    depend, support = fall(bricks)
    answer = []
    for start in range(len(depend)):
        seen = {start}
        frontier = [start]
        while frontier:
            current = frontier.pop()
            for p in support[current]:
                if p in seen:
                    continue
                if depend[p] - seen:
                    continue
                frontier.append(p)
                seen.add(p)
        answer.append(len(seen) - 1)
    return sum(answer)

print(part_one())
print(part_two())