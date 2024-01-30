from time import time

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9'
}

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

def findFirstNumber(line, reverse=False, part1=True):
    line = line[::-1] if reverse else line

    if part1:
        return findFirstNumberP1(line)
    else:
        return findFirstNumberP2(line, reverse)


def findFirstNumberP1(line):
    for c in line:
        if c.isnumeric():
            return c
        
    return None


def findFirstNumberP2(line, reversed):
    n = len(line)
    for index, c in enumerate(line):
        if c.isnumeric() :
            return c
        
        for number in digits:
            if (index + len(number) < n):
                s = line[index : index + len(number)]
                s = s[::-1] if reversed else s

                if s == number:
                    return digits[number]

    return None

@timer_func
def main(part1=True):
    with open("input.txt") as f:
        sum = 0
        for line in f.readlines():
            
            number1 = findFirstNumber(line=line, reverse=False, part1=part1)
            number2 = findFirstNumber(line=line, reverse=True, part1=part1)

            number = number1 + number2 
            sum += int(number)
        
        return sum


if __name__ == "__main__":
    print("Answer Task 1: {}".format(main(True)))
    print("Answer Task 2: {}".format(main(False)))




