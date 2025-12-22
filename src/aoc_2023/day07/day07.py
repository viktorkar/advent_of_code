from collections import Counter
from functools import cmp_to_key
from time import time
import re

CARDS = "23456789TJQKA"
CARDS_P2 = "J23456789TJQKA"


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        return result

    return wrap_func


def get_data():
    with open("input.txt") as f:
        regex = r"(\w{5}) (\d+)"
        hands = re.findall(regex, f.read())
        return hands


def get_hand_type(hand):
    counts = sorted(Counter(hand).values(), reverse=True)
    if counts[0] == 5:
        return 6
    if counts[0] == 4:
        return 5
    if counts[0] == 3 and counts[1] == 2:
        return 4
    if counts[0] == 3:
        return 3
    if counts[0] == 2 and counts[1] == 2:
        return 2
    if counts[0] == 2:
        return 1
    return 0


def get_hand_type_p2(hand):
    jokers = hand.counts("J")
    hand = [card for card in hand if card != "J"]
    counts = sorted(Counter(hand).values(), reverse=True)
    if not counts:
        counts = [0]
    if counts[0] + jokers == 5:
        return 6
    if counts[0] + jokers == 4:
        return 5
    if counts[0] + jokers == 3 and counts[1] == 2:
        return 4
    if counts[0] + jokers == 3:
        return 3
    if counts[0] == 2 and (jokers or counts[1] == 2):
        return 2
    if counts[0] == 2 or jokers:
        return 1
    return 0


def compare(a, b):
    type_a = get_hand_type(a[0])
    type_b = get_hand_type(b[0])
    if type_a > type_b:
        return 1
    if type_a < type_b:
        return -1
    for card_a, card_b in zip(a[0], b[0]):
        if card_a == card_b:
            continue
        a_wins = CARDS.index(card_a) > CARDS.index(card_b)
        return 1 if a_wins else -1


@timer_func
def solve():
    hands = get_data()
    hands.sort(key=cmp_to_key(compare))

    total = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        total += rank * int(bid)

    return total


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve()))
    # print("Answer Task 2: {}".format(solve(True)))
