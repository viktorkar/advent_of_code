
def get_input(line):
    assignment1, assignment2 = line.split(",")
    sec1_start, sec1_stop = assignment1.split("-")
    sec2_start, sec2_stop = assignment2.split("-")

    return int(sec1_start), int(sec1_stop), int(sec2_start), int(sec2_stop)

################################################################################################
def fully_contains_other(sec1_start, sec1_stop, sec2_start, sec2_stop):
    # First check if the first section contains the second
    if sec1_start <= sec2_start and sec1_stop >= sec2_stop:
        return True
    
    # Then scheck if the second second contains the first
    if sec2_start <= sec1_start and sec2_stop >= sec1_stop:
        return True

    return False

################################################################################################
def overlap_each_other(sec1_start, sec1_stop, sec2_start, sec2_stop):
    # First check if the first section has overlap with the second
    if sec1_start <= sec2_start and sec1_stop >= sec2_start:
        return True
    
    # Then scheck if the second second has overlap with the first
    if sec2_start <= sec1_start and sec2_stop >= sec1_start:
        return True

    return False

################################################################################################
def solve_task1(filename):
    counter = 0

    with open(filename) as f:
        for line in f:
            sec1_start, sec1_stop, sec2_start, sec2_stop = get_input(line.strip())

            if fully_contains_other(sec1_start, sec1_stop, sec2_start, sec2_stop):
                counter += 1
            
    print("Number of assignments pairs containing the other:", counter)

################################################################################################
def solve_task2(filename):
    counter = 0

    with open(filename) as f:
        for line in f:
            sec1_start, sec1_stop, sec2_start, sec2_stop = get_input(line.strip())

            if overlap_each_other(sec1_start, sec1_stop, sec2_start, sec2_stop):
                counter += 1
            
    print("Number of assignments pairs overlapping each other:", counter)

solve_task1("input.txt")
solve_task2("input.txt")