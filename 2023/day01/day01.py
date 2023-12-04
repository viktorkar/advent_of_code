
digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine' : 9
}

def findFirstNumberPart1(line):
    for c in line:
        if c.isnumeric():
            return c
        
    return None

def findFirstNumberPart2(line):
    for index, c in enumerate(line):
        
        if c.isnumeric() :
            return c
        
        for digit, value in digits:
            if (index + len(digit))
            s = line[index, index+len(digit)]
        
    return None



with open("input.txt") as f:
    sum = 0
    for line in f.readlines():
        
        number1 = findFirstNumberPart1(line)
        number2 = findFirstNumberPart1(reversed(line))

        number = number1 + number2 
        sum += int(number)
    
    print("Answer: ", sum)

