from collections import defaultdict
with open('14/14.txt', 'r') as file:
    data = file.read().strip()


def run_cyle(seq):
    seq_split = seq.split('#')
    new_seq = []
    for block in seq_split:
        char_count = block.count('O')
        block = 'O' * char_count + block.replace('O', '')
        new_seq.append(block)

    new_seq_str = '#'.join(new_seq)
    return new_seq_str


def part_one():
    vals = [row for row in data.split('\n')]

    columns = [''.join(column) for column in zip(*vals)]

    adj_cols = []
    for col in columns:
        sq_split = col.split('#')
        new_col = []
        for block in sq_split:
            char_count = block.count('O')
            block = 'O' * char_count + block.replace('O', '')
            new_col.append(block)

        new_col_str = '#'.join(new_col)
        adj_cols.append(new_col_str)

    adj_rows = [''.join(row) for row in zip(*adj_cols)]
    total_num = 0
    for i, row in enumerate(reversed(adj_rows), start=1):
        total_num += row.count('O') * i 
    
    return total_num

def part_two():
    vals = [row for row in data.split('\n')]
    og_vals = [row for row in data.split('\n')]
    i = 0
    seen = defaultdict(list)
    while i < 1000000000: 
        adj_vals = []
        # North
        vals = [''.join(val) for val in zip(*vals)]
        for val in vals:
            adj_vals.append(run_cyle(val)) 

        # West
        vals = [''.join(val) for val in zip(*adj_vals)]
        adj_vals = []
        for val in vals:
            adj_vals.append(run_cyle(val))
        
        # South
        vals = [''.join(val) for val in zip(*adj_vals)]
        adj_vals = []
        for val in vals:
            val = val[::-1]
            val = run_cyle(val)[::-1]
            adj_vals.append(val)
        
        #East
        vals = [''.join(val) for val in zip(*adj_vals)]
        adj_vals = []
        for val in vals:
            val = val[::-1]
            val = run_cyle(val)[::-1]
            adj_vals.append(val)
        
        vals = adj_vals
        seen[tuple(vals)].append(i)
        # print(sorted(seen.values()))
        if i == 149:
            total_num = 0
            for i, row in enumerate(reversed(vals), start=1):
                total_num += row.count('O') * i 
            return total_num
        i += 1

# print([index + i * 59 for i in range((1000 - index) // 59 + 1)])
print(part_one())
print(part_two())
