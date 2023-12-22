from collections import Counter
from decimal import Decimal
from random import sample

SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]
RANKS = [i for i in range(1, 14)]
DECK = [(suit, rank) for suit in SUITS for rank in RANKS]


def search_pair(hand: list):
    counter = dict(Counter([card[1] for card in hand]))
    for val in counter.values():
        if val >= 2:
            return True
    return False


def search_two_pairs(hand: list):
    counter = dict(Counter([card[1] for card in hand]))
    pairs = 0
    for val in counter.values():
        pairs += val // 2
        if pairs >= 2:
            return True
    return False


def search_three_kind(hand: list):
    counter = dict(Counter([card[1] for card in hand]))
    for val in counter.values():
        if val >= 3:
            return True
    return False


def search_straight(hand: list):
    VALID_CARDS_REQUIRED = 5
    len_hand = len(hand)
    if len_hand < VALID_CARDS_REQUIRED:
        return False
    sort_cards = sorted([card[1] for card in hand])
    i = 0
    valid_cards = 1
    new_start = False
    while i < len_hand:
        next_i = (i + 1) % len_hand
        if (sort_cards[next_i] - sort_cards[i]) % 13 == 1:
            valid_cards += 1
        elif new_start:
            return False
        else:
            valid_cards = 1
        i = next_i
        if i == 0:
            new_start = True
        if valid_cards == VALID_CARDS_REQUIRED:
            return True
    return False


def search_flush(hand: list):
    counter = dict(Counter([card[0] for card in hand]))
    for val in counter.values():
        if val >= 5:
            return True
    return False


def search_full_house(hand: list):
    counter = dict(Counter([card[1] for card in hand]))
    find_three_kind = False
    find_pair = False
    for val in counter.values():
        if val == 2:
            find_pair =True
        elif val >= 3:
            if find_pair:
                return True
            find_three_kind = True
        if val >= 2 and find_three_kind:
            return True
    return find_pair and find_three_kind


def search_four_kind(hand: list):
    counter = dict(Counter([card[1] for card in hand]))
    for val in counter.values():
        if val >= 4:
            return True
    return False


def search_straight_flush(hand: list):
    for suit in SUITS:
        if search_straight(list(filter(lambda x: x[0] == suit, hand))):
            return True
    return False


def search_royal_flush(hand: list):
    for suit in SUITS:
        suit_cards = [card[1] for card in filter(lambda x: x[0] == suit, hand)]
        if all(card in suit_cards for card in [1, 10, 11, 12, 13]):
            return True
    return False


def main():
    size_hand = int(input("Size hand?: "))
    n_simulations = int(input("N simulations?: "))

    total = {
        'pair': Decimal(0),
        'two_pairs': Decimal(0),
        'three_kind': Decimal(0),
        'straight': Decimal(0),
        'flush': Decimal(0),
        'full_house': Decimal(0),
        'four_kind': Decimal(0),
        'straight_flush': Decimal(0),
        'royal_flush': Decimal(0),
    }

    for _ in range(n_simulations):
        hand = sample(DECK, size_hand)
        if search_pair(hand):
            total['pair'] = total.get('pair') + 1
        if search_two_pairs(hand):
            total['two_pairs'] = total.get('two_pairs') + 1
        if search_three_kind(hand):
            total['three_kind'] = total.get('three_kind') + 1
        if search_straight(hand):
            total['straight'] = total.get('straight') + 1
        if search_flush(hand):
            total['flush'] = total.get('flush') + 1
        if search_full_house(hand):
            total['full_house'] = total.get('full_house') + 1
        if search_four_kind(hand):
            total['four_kind'] = total.get('four_kind') + 1
        if search_straight_flush(hand):
            total['straight_flush'] = total.get('straight_flush') + 1
        if search_royal_flush(hand):
            total['royal_flush'] = total.get('royal_flush') + 1

    for key, value in total.items():
        print(f'Probabilities of {key}: {value/Decimal(n_simulations)}')


if __name__ == "__main__":
    main()
