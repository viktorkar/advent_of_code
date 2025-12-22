import re


def read_input():
    data = []
    with open("input.txt") as f:
        for Line in f.read().splitlines():
            data.append([int(number) for number in re.findall(r"-?\d+", Line)])

    return data


def solve_p1():
    data = read_input()
    result = 0

    for numbers in data:
        final_numbers = []
        current_numbers = numbers

        while set(current_numbers) != set([0]):
            final_numbers.append(current_numbers[-1])
            current_numbers = [
                current_numbers[i] - current_numbers[i - 1] for i in range(1, len(current_numbers))
            ]

        result += sum(final_numbers)

    return result


def solve_p2():
    data = read_input()
    result = 0

    for numbers in data:
        final_numbers = []
        current_numbers = numbers

        while set(current_numbers) != set([0]):
            final_numbers.append(current_numbers[0])
            current_numbers = [
                current_numbers[i] - current_numbers[i - 1] for i in range(1, len(current_numbers))
            ]

        for i, number in enumerate(final_numbers):
            result += number if (i % 2 == 0) else -number

    return result


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve_p1()))
    print("Answer Task 2: {}".format(solve_p2()))