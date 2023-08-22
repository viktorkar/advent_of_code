import re

def get_input(filename):
    actions = []
    with open(filename) as f:
        data = f.readlines()
        moves = data[-1]
        world = data[:-1]

        pattern = r'(\d+|[LR])'
        actions = re.findall(pattern, moves)

        return world, actions
    
def turn(direction):
    current_direction = current_direction + 1 if direction is "R" else current_direction - 1
    current_direction %= 4

def move(num_steps):
    new_pos = current_pos
    if current_direction is 0: # Move UP
        pass
    elif current_direction is 1: # Move RIGHT
        world[current_pos[0]]
        pass
    elif current_direction is 2: # Move DOWN
        pass
    else: # Move LEFT
        pass

    current_pos = new_pos
    


world, actions = get_input("input.txt")
current_pos = (0, world[0].index("."))
current_direction = 1

for action in actions:
    if action.isDigit():
        move(action)
    else:
        turn(action)




