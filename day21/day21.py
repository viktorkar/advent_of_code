import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv, 
    '%' : operator.mod,
    '^' : operator.xor,
}

def get_input(filename):
    monkies_known = {}
    monkies_unknown = {}
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            monkey = line[0][:-1]

            if len(line) == 2:
                monkies_known[monkey] = int(line[1])
            else:
                monkies_unknown[monkey] = [line[1], line[2], line[3]]

    return monkies_known, monkies_unknown

def find_shout(monkey):
    if monkey in monkies_known:
        return monkies_known[monkey]
    else:
        monkey1, operator, monkey2 = monkies_unknown[monkey]
        value = ops[operator](find_shout(monkey1), find_shout(monkey2))
        #monkies_known[monkey] = value # can't be used for task2
        return value
    
# Task 1
monkies_known, monkies_unknown = get_input("input.txt")
answer_task1 = find_shout("root")
print(answer_task1)

#################################### Task 2 ##############################################
def find_value():
    rate = 0.01
    previous_guess = monkies_known["humn"]
    previous_error = abs(find_shout("root"))
    
    current_guess = 0
    monkies_known["humn"] = current_guess
    current_error = abs(find_shout("root"))

    while current_error > 0.1:
        # Calculate the slope of the function between the previous two guesses
        try:
            gradient = (current_guess - previous_guess) // (current_error - previous_error)
        except ZeroDivisionError:
            gradient = 1 if current_error < previous_error else -1

        # Remember the results of the guess
        previous_guess = current_guess
        previous_error = current_error

        # Update the guess
        current_guess -= rate * current_error * gradient
        monkies_known["humn"] = current_guess

        # Recalculate the error
        current_error = abs(find_shout("root"))
        print(current_error)
    
    print(current_guess)

# Task 2
monkies_known, monkies_unknown = get_input("input.txt")
monkies_unknown["root"][1] = "-"
find_value()

                            


