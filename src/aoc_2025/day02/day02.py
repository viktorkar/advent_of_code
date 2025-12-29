def read_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    return [(int(a), int(b)) for a, b in (pair.split("-") for pair in data.split(","))]


def length_is_even(num: str) -> bool:
    return len(num) % 2 == 0


def get_invalid_ids(id_range):
    result = []
    a, b = id_range

    for num in range(a, b + 1):
        number_str = str(num)
        if not length_is_even(number_str):
            continue

        mid = len(number_str) // 2
        left, right = number_str[:mid], number_str[mid:]

        if left == right:
            result.append(num)

    return result


def get_invalid_ids_p2(id_range):
    result = []
    a, b = id_range
    # TODO

    return result


def solve_p1():
    ranges = read_data("src/aoc_2025/day02/input.txt")
    total_sum = 0

    for range in ranges:
        invalid_ids = get_invalid_ids(range)
        total_sum += sum(invalid_ids)

    return total_sum


def solve_p2():
    ranges = read_data("src/aoc_2025/day02/input.txt")
    total_sum = 0

    for range in ranges:
        invalid_ids = get_invalid_ids_p2(range)
        total_sum += sum(invalid_ids)

    return total_sum


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
