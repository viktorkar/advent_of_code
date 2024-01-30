import numpy as np

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()

def get_starting_pos_of_rock(rock_type, y_top):
    y_lowest = y_top+4
    if rock_type == 1: # --
        return set([(x,y_lowest) for x in range(2,6)])
    if rock_type == 2: # +
        return set([(2, y_lowest+1), (3, y_lowest+1), (3, y_lowest), (4, y_lowest+1), (3, y_lowest+2)])
    if rock_type == 3: # _| 
        return set([(2, y_lowest), (3, y_lowest), (4, y_lowest), (4, y_lowest+1), (4, y_lowest+2)])
    if rock_type == 4: # |
        return set([(2, y) for y in range(y_lowest, y_lowest+4)])
    if rock_type == 5: # []
        return set([(2, y_lowest), (3, y_lowest), (2, y_lowest+1), (3, y_lowest+1)])

###########################################################################################################
def push_rock_right(rock_pos, occupied):
    new_pos = set([(x+1, y) for x,y in rock_pos])
    if max([x for x, _ in new_pos]) > 6 or new_pos & occupied: # if we can't push the rock anymore right -> return current pos
        return rock_pos
    else:
        return new_pos

###########################################################################################################
def push_rock_left(rock_pos, occupied):
    new_pos = set([(x-1, y) for x,y in rock_pos])
    if min([x for x, _ in new_pos]) < 0 or new_pos & occupied: # if we can't push the rock anymore left -> return current pos
        return rock_pos
    else:
        return new_pos

###########################################################################################################
def move_down(rock_pos, occupied):
    new_pos = set([(x,y-1) for x,y in rock_pos])

    return new_pos if not new_pos & occupied else None

###########################################################################################################
def solve_task1():
    jets = read_input("input.txt")
    n_jets = len(jets)
    occupied = set([(x, 0) for x in range(7)])
    y_top = 0
    jet_idx = 0

    for i in range(2022):
        rock_type = (i % 5) + 1

        # Set the rock at its starting position.
        pos = get_starting_pos_of_rock(rock_type, y_top)

        # Start falling
        while True:
            # Calculate pos after being pushed by jet
            jet = jets[jet_idx]
            jet_idx = (jet_idx + 1 ) % n_jets
            pos = push_rock_left(pos, occupied) if jet == "<" else push_rock_right(pos, occupied)

            # Try to move down
            new_pos = move_down(pos, occupied)

            # If we couldn't move down, add current poss to occupied and go to next stone
            if new_pos == None:
                occupied.update(pos)
                y_top = max(y_top, max([y for _, y in pos]))
                break
            else:
                pos = new_pos


    print("Solution task1: Highest point:", y_top)

solve_task1()