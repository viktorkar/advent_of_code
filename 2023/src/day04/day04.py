from time import time
import re
import math


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


def solve():
    with open("input.txt") as f:
        total_score = 0
        wins = []
        for line in f.read().splitlines():
            winning_numbers, my_numbers = line.split("|")

            winning_numbers = set(
                int(num) for num in re.findall(r"\b\d+\b", winning_numbers.split(":", 1)[1])
            )
            my_numbers = set(int(num) for num in re.findall(r"\b\d+\b", my_numbers))

            matching_numbers = len(winning_numbers.intersection(my_numbers))
            score = 0 if matching_numbers == 0 else 1 * math.pow(2, matching_numbers - 1)
            total_score += score
            wins.append(matching_numbers)

            print(matching_numbers)
            print(score)

    card_value = {}
    for card_id, won_cards in reversed(list(enumerate(wins))):
        card_value[card_id] = 1

        for id in range(card_id+1, card_id+won_cards+1):
            card_value[card_id] += card_value[id]

        print("Card " + str(card_id) + ": " + str(card_value[card_id]) + ", Wins: " + str(won_cards))

    return total_score, sum(card_value.values())


if __name__ == "__main__":
    p1, p2 = solve()
    print("Answer Task 1: {}".format(p1))
    print("Answer Task 2: {}".format(p2))
