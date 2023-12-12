with open('1/1.txt', 'r') as file:
    values = [line.strip() for line in file]

def part_one():
    digits = []
    for line in values:
        left, right = 0, len(line) - 1
        while True:
            if line[left].isdigit():
                left_val = str(line[left])
                break
            left += 1
        
        while True:
            if line[right].isdigit():
                right_val = str(line[right])
                break
            right -= 1

        value = left_val + right_val
        digits.append(int(value))
    return sum(digits)
    
def part_two():
    num_map = {
        'one': 'o1ne',
        'two': 't2wo',
        'three': 'thr3ee',
        'four': 'fo4ur',
        'five': 'fi5ve',
        'six': 'si6x',
        'seven': 'se7ven',
        'eight': 'ei8ght',
        'nine': 'ni9ne',
    }
    digits = []
    for line in values:
        for num, value in num_map.items():
            if num in line:
                line = line.replace(num, value)

        left, right = 0, len(line) - 1
        while True:
            if line[left].isdigit():
                left_val = str(line[left])
                break
            left += 1
        
        while True:
            if line[right].isdigit():
                right_val = str(line[right])
                break
            right -= 1

        value = left_val + right_val
        digits.append(int(value))
    return sum(digits) 
    
print(part_one())
print(part_two())