from collections import defaultdict

def read_input(filename):
    with open(filename) as f:
        return [line.strip().split(" ") for line in f.readlines()]

############################################################################################################
def calc_dir_sizes(current_index, current_dir):
    while current_index < len(input):
        line = input[current_index]

        if line[1] == "cd":                                      
            if line[2]   == "..": # If we want to move back -> We are done with this directory for now                       
                return current_index, directories[current_dir]
            else: # We want to move deeper -> Recursive call
                target_dir = current_dir + "/" + line[2]    
                current_index, target_size = calc_dir_sizes(current_index+1, target_dir)
                directories[current_dir] += target_size

        elif line[0].isnumeric(): # We have a size
            file_size = int(line[0])
            directories[current_dir] += file_size

        current_index += 1
    
    return current_index, directories[current_dir]

############################################################################################################
def solve_task1():
    global directories 
    global input 
    directories = defaultdict(int)
    input = read_input("input.txt")
    start_dir = "/"
    result = 0

    calc_dir_sizes(1, start_dir)

    for dir in directories:
        dir_size = directories[dir]
        #print("Directory: %s, size: %i" % (dir, dir_size))
        # For this task, we are only interested in directiories with sizes below 100000
        if dir_size <= 100_000:
            result += dir_size

    print("Solution to task1: Sum of directories =", result)

############################################################################################################
def solve_task2():
    global directories 
    global input 
    directories = defaultdict(int)
    input = read_input("input.txt")
    start_dir = "/"

    calc_dir_sizes(1, start_dir)

    total_memory = 70_000_000
    used_memory = directories[start_dir]
    required_memory = 30_000_000
    memory_to_free = required_memory - (total_memory - used_memory)

    print("Used space:", used_memory)
    print("Space required:", required_memory)
    print("Memory to free:", memory_to_free)

    best_dir_size = used_memory

    for dir in directories:
        dir_size = directories[dir]

        #print("Directory: %s, size: %i" % (dir, dir_size))
        # For this task, we are only interested in directiories with sizes below 100000
        if dir_size < best_dir_size and dir_size >= memory_to_free:
            best_dir_size = dir_size

    print("Solution to task2: Best dir size to remove", best_dir_size)


solve_task1()
solve_task2()


