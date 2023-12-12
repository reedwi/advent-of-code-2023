with open('6/6.txt', 'r') as file:
    data = file.read().strip()

times, distance = data.split('\n')
times = times.split()[1:]
distance = distance.split()[1:]
t_d = list(zip(times, distance))

def part_one():
    total_wins = 1
    for time, distance in t_d:
        time = int(time)
        distance = int(distance)
        left, right = 0, int(time)
        left_win, right_win = float('-inf'), float('-inf')
        wins = 0
        while left < right:
            distance_traveled = left * (time - left)
            if distance_traveled > distance:
                left_win = left
                break
            left += 1
        
        while right > 0:
            distance_traveled = right * (time - right)
            if distance_traveled > distance:
                right_win = right
                break
            right -= 1
        
        if left_win == right_win:
            wins += 1
        else:
            wins = right_win - left_win + 1
        total_wins *= wins
    return total_wins
        

def part_two():
    time, distance = data.split('\n')
    time = int(''.join([char for char in time if char.isdigit()]))
    distance = int(''.join([char for char in distance if char.isdigit()]))

    left, right = 0, time
    left_win, right_win = float('-inf'), float('-inf')
    wins = 0
    while left < right:
        distance_traveled = left * (time - left)
        if distance_traveled > distance:
            left_win = left
            break
        left += 1
    
    while right > 0:
        distance_traveled = right * (time - right)
        if distance_traveled > distance:
            right_win = right
            break
        right -= 1
    
    if left_win == right_win:
        wins += 1
    else:
        wins = right_win - left_win + 1
    return wins



print(part_one())
print(part_two())