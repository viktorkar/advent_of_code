import math

t = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
decode_map = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-"}


def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def convert_snafu(snafu_number: str) -> int:
    decimal_number = 0
    for i, ch in enumerate(reversed(snafu_number)):
        decimal_number += math.pow(5, i) * t[ch]

    return decimal_number


def convert_decimal(decimal_number: int) -> str:
    out = []
    while decimal_number:
        d = decimal_number % 5
        out.append(decode_map[d])

        if d == 3:
            decimal_number += 2
        elif d == 4:
            decimal_number += 1

        decimal_number //= 5
    return "".join(reversed(out))


def solve_task1():
    data = read_input("input.txt")
    sum_decimal = sum(map(convert_snafu, data))
    return convert_decimal(sum_decimal)


def main():
    print("Answer task 1: " + solve_task1())


if __name__ == "__main__":
    main()
