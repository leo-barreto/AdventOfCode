import sys
import math


# CARD_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_ORDER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def hand_value(hand):
    jokerhand = consider_joker(hand)
    counts = sorted([jokerhand.count(i) for i in set(jokerhand)])
    match counts:
        case [5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case [1, 1, 1, 1, 1]:
            return 1


def determine_rank(entries):
    points = [hand_value(hand[:5]) for hand in entries]
    zipped = sorted(list(zip(entries, points)), key=lambda x: x[1])
    return sort_draws(zipped)


def sort_draws(original):
    zipped = original.copy()
    i = 0
    while i < len(zipped) - 1:
        swapped = False
        handvalue = zipped[i][1]
        nexthandvalue = zipped[i + 1][1]
        if handvalue == nexthandvalue:
            if not solve_draw(zipped[i][0], zipped[i + 1][0]):
                zipped.insert(i + 1, zipped.pop(i))  # Swap positions
                swapped = True

        if swapped:
            i -= 1
        else:
            i += 1

    return zipped
    

def solve_draw(hand1, hand2):
    for i in range(5):
        value1 = CARD_ORDER.index(hand1[i])
        value2 = CARD_ORDER.index(hand2[i])
        if  value1 != value2: 
            values = [value1, value2]
            return values.index(max(values))


def consider_joker(hand):
    newhand = list(hand)
    counts = [hand.count(i) for i in CARD_ORDER[1:]]
    mostfrequent = CARD_ORDER[1 + counts.index(max(counts))]
    for i, c in enumerate(newhand):
        if c == 'J':
            newhand[i] = mostfrequent
    
    return ''.join(newhand)


inputfile = open(str(sys.argv[1]), 'r')
fullentry = [i.strip() for i in inputfile]

ranks = determine_rank(fullentry)
sortedbids = [int(hand[0].split()[1]) for hand in ranks]
print(sum([b * (i + 1) for i, b in enumerate(sortedbids)]))
