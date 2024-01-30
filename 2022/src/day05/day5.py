import numpy as np
import re
import queue

##########################################################################################################################
def read_input(filename):
    with open(filename) as f:
        return np.array(f.readlines())

##########################################################################################################################
def extract_start_state(input):
    starting_data = input[:8]
    start_state = []

    for line in starting_data:
        line_data = [line[i:i+4].strip() for i in range(0, len(line), 4)]
        line_data = [re.sub(r"[\[\]]" , "", x) for x in line_data] # Remove brackets from string
        start_state.append(line_data)

    return np.array(start_state)

##########################################################################################################################
def extract_operations(input):
    operations = input[10:len(input)]
    operations = [re.sub(r"[^0-9]+", " ", line) for line in operations] # Remove everything except the numbers
    operations = [line.strip().split(" ") for line in operations]       # Split the numbers and remove leading and trailing whitespaces
    operations = [list(map(int, line)) for line in operations]       # Split the numbers and remove leading and trailing whitespaces

    return operations

##########################################################################################################################
def build_stacks(start_state):
    stacks = []
    n_stacks = start_state.shape[1]

    # Create the FIFO-queues
    for i in range(n_stacks):
        stacks.append(queue.LifoQueue())

    # Add the starting position
    for line in reversed(start_state):
        for stack_id, crate in enumerate(line):
            if crate:
                stacks[stack_id].put(crate)
    
    return stacks

##########################################################################################################################
def perform_operation_crateMover9000(stacks, operation):
    crates_to_move, from_id, to_id = operation

    for i in range(crates_to_move):
        crate = stacks[from_id-1].get()
        stacks[to_id-1].put(crate)
        print("Moved %s from %i to %i" % (crate, from_id, to_id))

    return stacks

##########################################################################################################################
def perform_operation_crateMover9001(stacks, operation):
    crates_to_move, from_id, to_id = operation
    moved_block = []

    for i in range(crates_to_move):
        moved_block.append(stacks[from_id-1].get())
    
    for crate in reversed(moved_block):
        stacks[to_id-1].put(crate)
    
    print("Moved block %s from %i to %i" % (moved_block, from_id, to_id))

    return stacks

##########################################################################################################################
def solve_task1():
    input = read_input("input.txt")
    start_state = extract_start_state(input)
    operations = extract_operations(input)
    stacks = build_stacks(start_state)

    for operation in operations:
        stacks = perform_operation_crateMover9000(stacks, operation)
    
    # Get the top crate of each stack
    result = []
    for stack in stacks:
        result.append(stack.get())

    print("Task1: Resulting crates on top:", result)

##########################################################################################################################
def solve_task2():
    input = read_input("input.txt")
    start_state = extract_start_state(input)
    operations = extract_operations(input)
    stacks = build_stacks(start_state)

    for operation in operations:
        stacks = perform_operation_crateMover9001(stacks, operation)
    
    # Get the top crate of each stack
    result = []
    for stack in stacks:
        result.append(stack.get())

    print("Task2: Resulting crates on top:", result)

    
solve_task1()
solve_task2()


