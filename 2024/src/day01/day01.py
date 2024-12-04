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


def get_data(filename):
    col_1, col_2 = [], []
    with open(filename) as file:
        for line in file.readlines():
            val_1, val_2 = [int(val) for val in line.split('   ')]
            col_1.append(val_1)
            col_2.append(val_2)

    return col_1, col_2

@timer_func
def solve_p1():
    col_1, col_2 = get_data('input.txt')
    col_1.sort()
    col_2.sort()

    return sum([abs(col_1[i]-col_2[i]) for i in range(len(col_1))])


@timer_func
def solve_p2():
    col_1, col_2 = get_data("input.txt")
    col_1.sort()
    col_2.sort()

    sum = 0
    for num in col_1:
        occurances = col_2.count(num)
        sum += num * occurances
        
    return sum


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
