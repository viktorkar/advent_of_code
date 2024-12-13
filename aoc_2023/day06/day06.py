import re
from time import time


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


def get_data(part2=False):
    with open("input.txt") as f:
        lines = f.read().splitlines()

        times = [int(time) for time in re.findall(r"\b\d+\b", lines[0])]
        distances = [int(distance) for distance in re.findall(r"\b\d+\b", lines[1])]

        if part2:
            times = [int("".join(map(str, times)))]
            distances = [int("".join(map(str, distances)))]

        return list(zip(times, distances))


@timer_func
def solve(part2=False):
    races = get_data(part2)
    total = 1

    for time, distance in races:
        wins = 0
        speed = 0
        for acceleration in range(1, time):
            speed += 1
            travelled = speed * (time - acceleration)

            if travelled > distance:
                wins += 1
            elif wins:
                break

        total *= wins

    return total


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve()))
    print("Answer Task 2: {}".format(solve(True)))
