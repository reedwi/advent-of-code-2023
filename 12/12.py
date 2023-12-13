import functools

with open('12/12.txt', 'r') as file:
    data = file.read().strip()

vals = [[line.split()[0], list(map(int, line.split()[1].split(',')))] for line in data.split('\n')]


@functools.cache
def gen_options(size, splits):
    def gen(rem_len, rem_splits):
        if len(rem_splits) == 0:
            yield '.' * rem_len
            return

        a = rem_splits[0]
        rest = rem_splits[1:]
        after = sum(rest) + len(rest)

        for before in range(rem_len-after-a+1):
            cand = '.' * before + '#' * a + '.'
            for opt in gen(rem_len-a-before-1, rest):
                yield cand + opt

    return list(gen(size, splits))

def find_matches(pattern, splits):
    options = gen_options(len(pattern), tuple(splits))

    for o in options:
        if all((c0==c1 or c0=='?')
               for c0,c1 in zip(pattern, o)):
            yield o

def part_one():

    answer = 0

    for line, group in vals:
        answer += len(list(find_matches(line, group)))
    
    return answer



def part_two():

    return 


print(part_one())
print(part_two())


