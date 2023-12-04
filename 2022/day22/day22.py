import re

def get_input(filename):
    actions = []
    with open(filename) as f:
        data = f.readlines()
        moves = data[-1]
        world = data[:-1]
        num_rows = len(world[0])
        world = [row.replace("\n", "") + " " * (num_rows - len(row)) for row in world] # Make the rows uniform in lenght

        pattern = r'(\d+|[LR])'
        actions = re.findall(pattern, moves)

        return world, actions
    
def wrap_around():
    row, col = current_pos
    if current_direction == 3: # UP -> Wrap to bottom
        column_tiles = extract_col(col)
        row = len(column_tiles.rstrip()) - 1 # Remove trailing whitespaces and then get last index
    elif current_direction == 0: # RIGHT -> Wrap to left side
        row_tiles = world[row]
        col = find_start_index(row_tiles)
    elif current_direction == 1: # DOWN -> Wrap to top
        column_tiles = extract_col(col)
        row = find_start_index(column_tiles)
    else: # LEFT -> Wrap to right side
        row_tiles = world[row]
        col = len(row_tiles.rstrip()) - 1

    return row, col

def extract_col(col):
    column_tiles = ""
    for row in world:
        column_tiles += row[col]
    return column_tiles

def find_start_index(s):
    for index, c in enumerate(s):
        if c != " ":
            return index
    
    return -1
    
def paint_world(row, col):
    symbol = ""
    if current_direction == 0: # RIGHT
        symbol = ">"
    elif current_direction == 1: # DOWN
        symbol = "v"
    elif current_direction == 2: # LEFT
        symbol = "<"
    else: # UP
        symbol = "^"

    world[row] = world[row][:col] + symbol + world[row][col + 1:]

def is_out_of_bounds(row, col):
    return row < 0 or row > max_row or col < 0 or col > max_col or world[row][col] == " "

def is_wall(row, col):
    return world[row][col] == "#"
    
def turn(direction):
    global current_direction
    current_direction = current_direction + 1 if direction == "R" else current_direction - 1
    current_direction = (current_direction + 4) % 4
    print(current_direction)

def move(num_steps):
    global current_pos
    row, col = current_pos
    row_change, col_change = direction_changes[current_direction]

    for i in range(num_steps):
        row += row_change
        col += col_change

        if is_out_of_bounds(row, col):
            row, col = wrap_around()

        # If we hit a wall, stop the movement, else update current pos
        if is_wall(row, col):
            break
        else:
            current_pos = (row, col)
            paint_world(row, col)
            #print(current_pos)


def print_world(filename):
    with open(filename, "w") as file:
        # Iterate through the array and write each element to a new line
        for row in world:
            file.write(row + "\n")  # Add a newline character at the end
            

    
world, actions = get_input("input.txt")
current_pos = (0, world[0].index("."))
current_direction = 0
min_row, max_row = 0, len(world) - 1
min_col, max_col = 0, len(world[0]) - 1


direction_changes = {
    3: (-1, 0),  # UP
    0: (0, 1),   # RIGHT
    1: (1, 0),   # DOWN
    2: (0, -1)   # LEFT
}

count = 0
for action in actions:
    if action.isdigit():
        move(int(action))
    else:
        turn(action)

    #count += 1
    if (count > 5):
        break

answer = (current_pos[0]+1) * 1000 + (current_pos[1]+1) * 4 + current_direction
print(current_pos)
print(answer)
print_world("output.txt")




