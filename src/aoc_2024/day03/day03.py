import re

regex_pattern = 'mul\((-?\d*\.?\d+),\s*(-?\d*\.?\d+)\)'
enable_mul = 'do()'
disable_mul = "don't()"

def get_data(filename):
    with open(filename) as f:
        multiples = re.findall(regex_pattern, f.read())
        return [(int(x), int(y)) for x, y in multiples]


def filter_data_string(data: str):
    disable_from = data.find(disable_mul)
    while disable_from != -1:
        disable_to = data[disable_from:].find(enable_mul)

        if (disable_to == -1):
            data = data[:disable_from]
        else:
            disable_to = disable_to + disable_from
            data = data[:disable_from] + data[disable_to:]

        disable_from = data.find(disable_mul)

    return data


def get_data_p2(filename):
    with open(filename) as f:
        filtered_data = filter_data_string(f.read())

        multiples = re.findall(regex_pattern, filtered_data)
        return [(int(x), int(y)) for x, y in multiples]


def solve_p1():
    data = get_data('input.txt')
    return sum([x*y for x, y in data])


def solve_p2():
    data = get_data_p2("input.txt")
    return sum([x * y for x, y in data])


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))

    test = "don't()hejhejdo()nejnejdon't()okejokejdo()tedon't()"
    print(filter_data_string(test))
