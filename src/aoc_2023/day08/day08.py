import re
import math
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


def read_data():
    pattern = r"\b\w+\b"
    data = {}

    with open("input.txt") as f:
        instructions, mappings = f.read().split("\n\n")

        for mapping in mappings.split("\n"):
            mapping = re.findall(pattern, mapping)
            data[mapping[0]] = mapping[1:]

        return [c for c in instructions], data


def find_number_of_steps(start_node, instructions, mappings, part2=False):
    current_value = start_node
    instruction_id = 0
    result = 0

    while (not part2 and current_value != "ZZZ") or (part2 and not current_value.endswith("Z")):
        instuction = 0 if instructions[instruction_id] == "L" else 1
        current_value = mappings[current_value][instuction]

        instruction_id = (instruction_id + 1) % len(instructions)
        result += 1

    return result


@timer_func
def solve_p1():
    instuctions, mappings = read_data()
    return find_number_of_steps("AAA", instuctions, mappings)


@timer_func
def solve_p2():
    instuctions, mappings = read_data()
    keys_ending_with_A = [key for key in mappings.keys() if key.endswith("A")]
    result = 1

    for value in keys_ending_with_A:
        result = math.lcm(result, find_number_of_steps(value, instuctions, mappings, part2=True))

    return result


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve_p1()))
    print("Answer Task 2: {}".format(solve_p2()))
