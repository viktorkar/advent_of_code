def read_data(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()
    return [line.strip() for line in data]


def solve_p1():
    data = read_data("src/aoc_2025/day01/input.txt")

    initial_value = 50

    answer = 0

    for rotation in data:
        direction, amount = rotation[0], int(rotation[1:])

        if direction == "L":
            initial_value = (initial_value - amount) % 100
        elif direction == "R":
            initial_value = (initial_value + amount) % 100

        if initial_value == 0:
            answer += 1

    return answer


def count_zero_hits(start: int, delta: int) -> int:
    end = start + delta

    if delta > 0:
        return max(0, end // 100 - start // 100)
    else:
        return max(0, (start - 1) // 100 - (end - 1) // 100)


def solve_p2() -> int:
    value = 50
    hits = 0

    for r in read_data("src/aoc_2025/day01/input.txt"):
        direction, amount = r[0], int(r[1:])
        delta = amount if direction == "R" else -amount

        hits += count_zero_hits(value, delta)
        value = (value + delta) % 100

    return hits


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
