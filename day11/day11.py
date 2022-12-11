import numpy as np
import math

##########################################################################################################################
def read_input(filename):
    with open(filename) as f:
        return np.array([x.strip() for x in f.readlines()])

##########################################################################################################################
def setup(input):
    # Extract starting items
    starting_items = [x.replace(",", "").split(" ")[2:] for x in input if "Starting items:" in x]
    starting_items = [list(map(int, x)) for x in starting_items]
    print("Starting items:\n", starting_items)

    # Extracts operations
    operations = [x.split(" ")[-2:] for x in input if "Operation:" in x]
    print("\nOperations:\n", operations)
    
    # Extract tests
    tests = [int(x.split(" ")[-1]) for x in input if "Test:" in x]
    print("\nTests:\n", tests)

    # Extract actions, first index is "if true", second is "if false"
    actions_true= [int(x.split(" ")[-1]) for x in input if "true:" in x]
    actions_false = [int(x.split(" ")[-1]) for x in input if "false:" in x]
    actions = list(zip(actions_true, actions_false))
    print("\nActions:\n", actions)

    return starting_items, operations, tests, actions
    
###############################################################################################
def get_worry_level(item, operation, value):
    value = int(value) if value != "old" else item

    if operation == "+":
        return item + value
    elif operation == "-":
        return item - value
    elif operation == "*":
        return item * value

###############################################################################################
def solve_task1():
    input = read_input("input.txt")
    items, operations, tests, actions = setup(input)

    n_rounds = 10000
    n_monkeys = len(items)
    n_inspections = [0] * n_monkeys

    for round in range(n_rounds):
        for monkey in range(n_monkeys):
            for i in range(len(items[monkey])):
                item = items[monkey].pop(0)
                operation, value = operations[monkey]
                test = tests[monkey]
                action = actions[monkey]

                worry_level = get_worry_level(item, operation, value)
                worry_level = int(worry_level / 3)

                # Get action by checking the outcome of the test
                throw_to_monkey = action[0] if (worry_level % test) == 0 else action[1]

                # Throw the item to another monkey
                items[throw_to_monkey].append(worry_level)

                n_inspections[monkey] += 1
    
    for monkey, inspections in enumerate(n_inspections):
        print("Monkey %i inspected %i items." % (monkey, inspections))

###############################################################################################
def solve_task2():
    input = read_input("input.txt")
    items, operations, tests, actions = setup(input)

    n_rounds = 10000
    n_monkeys = len(items)
    n_inspections = [0] * n_monkeys
    supermodulo = math.prod(tests)

    for round in range(n_rounds):
        for monkey in range(n_monkeys):
            for i in range(len(items[monkey])):
                item = items[monkey].pop(0)
                operation, value = operations[monkey]
                test = tests[monkey]
                action = actions[monkey]

                worry_level = get_worry_level(item, operation, value)
                worry_level = worry_level % supermodulo

                # Get action by checking the outcome of the test
                throw_to_monkey = action[0] if (worry_level % test) == 0 else action[1]

                # Throw the item to another monkey
                items[throw_to_monkey].append(worry_level)
                n_inspections[monkey] += 1
    
    for monkey, inspections in enumerate(n_inspections):
        print("Monkey %i inspected %i items." % (monkey, inspections))

solve_task1()
solve_task2()


    

