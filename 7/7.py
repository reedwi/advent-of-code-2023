

with open('7/7.txt', 'r') as file:
    data = file.read().strip()

lines = data.split('\n')
values = [(game.split()[0], game.split()[1]) for game in lines]
possible_cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def insert_hand(hand, bid, card_category, card_categories, possible_cards):
    for i, (loop_hand, loop_bid) in enumerate(card_categories[card_category]):
        for j in range(5):
            loop_card_index = possible_cards.index(loop_hand[j])
            hand_card_index = possible_cards.index(hand[j])

            if loop_card_index > hand_card_index:
                break  # This hand is not stronger, move to the next one
            elif loop_card_index < hand_card_index:
                card_categories[card_category].insert(i, (hand, bid))
                return card_categories  # Hand inserted, return the updated categories
            else:  # If we didn't break, the hands are equal and we check the next card
                continue

    # If the hand is not inserted yet, it is the weakest, append it
    card_categories[card_category].append((hand, bid))
    return card_categories


def part_one():
    card_categories = {
        "H": [],
        "1P": [],
        "2P": [],
        "3": [],
        "FH": [],
        "4": [],
        "5": []
    }
    for hand, bid in values:
        hand_set = set(hand)
        counts = [hand.count(card) for card in hand_set]
        
        if len(hand_set) == 1:
            card_categories = insert_hand(hand, bid, '5', card_categories, possible_cards)
        elif len(hand_set) == 2 and 3 in counts:
            card_categories = insert_hand(hand, bid, 'FH', card_categories, possible_cards)
        elif len(hand_set) == 2 and 4 in counts:
            card_categories = insert_hand(hand, bid, '4', card_categories, possible_cards)
        elif len(hand_set) == 3 and 3 in counts:
            card_categories = insert_hand(hand, bid, '3', card_categories, possible_cards)
        elif len(hand_set) == 4:
            card_categories = insert_hand(hand, bid, '1P', card_categories, possible_cards)
        elif len(hand_set) == 5:
            card_categories = insert_hand(hand, bid, 'H', card_categories, possible_cards)
        else:
            card_categories = insert_hand(hand, bid, '2P', card_categories, possible_cards)

    ordered_options = []
    for card_category in card_categories:
        ordered_options.extend(reversed(card_categories[card_category]))

    total_values = 0
    for i, ordered_option in enumerate(ordered_options, start=1):
        total_values += int(ordered_option[1]) * i

    return total_values



def categorize_with_jokers(hand, jokers, counts):
    if jokers == 5:
        return '5'  # All cards are jokers, highest category
    
    # Sort counts in descending order, ignoring zeros
    sorted_counts = sorted([c for c in counts if c > 0], reverse=True)

    # Use jokers to enhance existing card types first
    for i in range(len(sorted_counts)):
        while jokers > 0 and (i == 0 or sorted_counts[i-1] - sorted_counts[i] > 1):
            sorted_counts[i] += 1
            jokers -= 1

    sorted_counts.sort(reverse=True)  # Re-sort after enhancing

    if sorted_counts[0] == 5:
        return '5'
    elif sorted_counts[0] == 4:
        return '4'
    elif sorted_counts[0] == 3:
        if len(sorted_counts) > 1 and sorted_counts[1] >= 2:
            return 'FH'
        return '3'
    elif sorted_counts[0] == 2:
        if len(sorted_counts) > 1 and sorted_counts[1] == 2:
            return '2P'
        return '1P'
    else:
        return 'H'


def part_two():
    card_categories = {
        "H": [],
        "1P": [],
        "2P": [],
        "3": [],
        "FH": [],
        "4": [],
        "5": []
    }
    for hand, bid in values:
        jokers = hand.count('J')
        hand_set = set(hand) - {'J'}
        counts = [hand.count(card) for card in hand_set]

        best_category = categorize_with_jokers(hand, jokers, counts)
        card_categories = insert_hand(hand, bid, best_category, card_categories, possible_cards)
        
    ordered_options = []
    for card_category in card_categories:
        ordered_options.extend(reversed(card_categories[card_category]))

    total_values = 0
    for i, ordered_option in enumerate(ordered_options, start=1):
        total_values += int(ordered_option[1]) * i

    return total_values


print(part_one())
print(part_two())