from collections import defaultdict
with open('4/4.txt', 'r') as file:
    values = [line.strip() for line in file]

def part_one():
    total_points = []
    for line in values:
        remove_card_num = line.split(':')[1]
        split_card = remove_card_num.split('|')
        cards = [[num for num in card.strip().split(' ') if num] for card in split_card]
        
        my_card, winning_nums = cards[0], cards[1]
        count = 0
        for num in my_card:
            if num in winning_nums:
                count += 1
        if count > 0:
            total_points.append(2 ** (count-1))
    return sum(total_points)

def part_two():
    collected_cards = defaultdict(int)
    for i, line in enumerate(values, start=1):
        remove_card_num = line.split(':')[1]
        split_card = remove_card_num.split('|')
        cards = [[num for num in card.strip().split(' ') if num] for card in split_card]
        
        my_card, winning_nums = cards[0], cards[1]
        count = 0
        for num in my_card:
            if num in winning_nums:
                count += 1
        
        for j in range(count):
            collected_cards[j + i + 1] += collected_cards[i]

    return sum(collected_cards.values())


print(part_one())
print(part_two())