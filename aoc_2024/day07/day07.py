

import operator


def get_data(filename):
    with open(filename) as f:
        return [
            (int(target), [int(number) for number in numbers.strip().split()])
            for target, numbers in (line.split(":") for line in f)
        ]

def can_be_calibrated(target, numbers, operators=(operator.add, operator.mul)):
    first, *rest = numbers
    results = {first}
    for y in rest:
        results = {op(x, y) for x in results if x <= target for op in operators}
    return target in results

    
def solve_p1():
    data = get_data('input.txt')
    result = 0

    for target, numbers in data:
        if can_be_calibrated(target, numbers):
            result += target
    
    return result

def solve_p2():
    data = get_data('input.txt')
    result = 0
    operators3 = (operator.add, operator.mul, lambda x, y: int(str(x) + str(y)))

    for target, numbers in data:

        if can_be_calibrated(target, numbers, operators3):
            result += target
    
    return result



if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
