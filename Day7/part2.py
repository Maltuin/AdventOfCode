import re

def take_first(elem):
    return elem[1]

all_hands = {
    "none" : [],
    "onepair" : [],
    "twopair" : [],
    "threeofakind" : [],
    "fullhouse" : [],
    "fourofakind" : [],
    "fiveofakind" : []
}

card_value = dict(zip('J 2 3 4 5 6 7 8 9 T Q K A'.split(), range(14)))

for line in open("data.txt", "r"):
    cards, value = line.replace('\n', '').split(" ")
    
    same_cards = sorted([cards.count(a) for a in set(cards)])
    card_nums = [card_value[a] for a in cards]
    
    max_same_cards = max(same_cards)
    len_same_cards = len(same_cards)
    data = (cards, card_nums, int(value))
    
    if len_same_cards == 1:
        all_hands["fiveofakind"].append(data)
    elif len_same_cards == 2:
        if max_same_cards == 3:
            all_hands["fullhouse"].append(data)
        else:
            all_hands["fourofakind"].append(data)
    elif len_same_cards == 3:
        if max_same_cards == 3:
            all_hands["threeofakind"].append(data)
        else:
            all_hands["twopair"].append(data)
    elif len_same_cards == 4:
        all_hands["onepair"].append(data)
    else:
        all_hands["none"].append(data)

total = 0
count = 1

for hand in all_hands.values():
    hand.sort(key=take_first)
    for handbyhand in hand:
        total += handbyhand[2] * count
        count += 1

print(total)