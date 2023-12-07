
hands = []
bets = []

cards = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def load_input():
    global hands, bets
    for line in open('input.txt').readlines():
        hand, bet = line.split(' ')
        hands.append(hand)
        get_hand_type(hand)
        bets.append(int(bet))

def get_hand_type(hand):
    counts = { c: hand.count(c) for c in hand }
    cardvals = len(counts.items())
    if cardvals == 1:
        return 700000 # Five of a kind
    elif cardvals == 2:
        if list(counts.items())[0] == 1 or list(counts.items())[0] == 4:
            return 600000 # Four of a kind
        else:
            return 500000 # Full house
    elif cardvals == 3:
        if any([v == 3 for v in counts.items()]):
            return 400000 # Three of a kind
        else:
            return 300000 # Two pair
    elif cardvals == 4:
        return 200000 # One pair
    else:
        return 100000 # High card

def get_total_value(hand):
    val = 0
    for idx, c in enumerate(hand):
        val += cards[c]*(10**idx)
    print(val + get_hand_type(hand))
    return val + get_hand_type(hand)

load_input()
games = zip(hands, bets)
total = 0
games = sorted(games, key=lambda g: get_total_value(g[0]))
print(games)
for idx, game in enumerate(games):
    total += game[1] * (idx+1)
print(total)