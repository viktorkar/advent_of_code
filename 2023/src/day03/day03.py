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


def get_data(file_path="input.txt"):
    symbol_positions = set()
    numbers = []
    gears = {}

    with open(file_path) as f:
        for row, line in enumerate(f):
            line = line.strip()
            number, i, j = "", -1, -1

            for col, char in enumerate(line):
                if char.isdigit():
                    if not number:
                        i, j = row, col
                    number += char
                else:
                    if number:
                        numbers.append((number, i, j))
                        number, i, j = "", -1, -1

                    if char != ".":
                        symbol_positions.add((row, col))

                    if char == "*":
                        gears[(row, col)] = []

            if number:
                numbers.append((number, i, j))

    return numbers, symbol_positions, gears


def get_neighboring_points(number_data):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    number, row, col_start = number_data
    col_end = col_start + len(number)
    word_cols = range(col_start, col_end)

    return {(row + dr, col + dc) for col in word_cols for dr, dc in neighbors}


@timer_func
def solve():
    sum = 0
    gear_ratios = 0
    numbers, symbol_positions, gears = get_data()

    for number_data in numbers:
        neighboring_points = get_neighboring_points(number_data)

        if any(point in symbol_positions for point in neighboring_points):
            sum += int(number_data[0])

        for point in neighboring_points:
            if point in gears:
                gears[point].append(int(number_data[0]))

    for connected_numbers in gears.values():
        if len(connected_numbers) == 2:
            gear_ratios += connected_numbers[0] * connected_numbers[1]

    return sum, gear_ratios


if __name__ == "__main__":
    p1, p2 = solve()
    print("Answer Task 1: {}".format(p1))
    print("Answer Task 2: {}".format(p2))
