NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
ELF = "#"
EMPTY_SPACE = "."

from pprint import pprint


def read_input(filename) -> tuple[list[str], set]:
    elf_positions = set()

    with open(filename) as f:
        grid = f.read().splitlines()

        for row, line in enumerate(grid):
            for col, ch in enumerate(line):
                if ch == ELF:
                    elf_positions.add((row, col))

        return grid, elf_positions


def get_direction(current_pos, new_pos):
    current_row, current_col = current_pos
    new_row, new_col = new_pos

    # Determine the direction of movement
    if new_row < current_row:
        return NORTH
    elif new_row > current_row:
        return SOUTH
    elif new_col < current_col:
        return WEST
    elif new_col > current_col:
        return EAST
    else:
        return None  # If the positions are the same, no direction


def get_proposed_move(round, current_pos, grid) -> tuple[int, int]:
    n_directions = len(direction_order)

    for i in range(n_directions):
        index = ((round % n_directions) + i) % n_directions
        direction = direction_order[index]
        row_change, col_change = direction_changes[direction]
        new_pos = current_pos[0] + row_change, current_pos[1] + col_change

        # Return the proposed move if it is possible to move there
        if is_valid_move(new_pos, direction, grid):
            return new_pos

    return None


def extract_col(col, row_start, row_end, grid) -> str:
    column_tiles = ""
    for row in range(row_start, row_end + 1):
        column_tiles += grid[row][col]
    return column_tiles


def is_valid_move(new_pos, direction, grid) -> bool:
    row, col = new_pos
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1

    # First check if new pos inside grid
    if row <= 0 or row > max_row or col <= 0 or col > max_col:
        return False

    # Check that we are not blocked by any elfs in that direction
    if direction == NORTH or direction == SOUTH:
        col_min, col_max = max(col - 1, 0), min(col + 1, max_col)
        return ELF not in grid[row][col_min : col_max + 1]
    else:
        row_min, row_max = max(row - 1, 0), min(row + 1, max_row)
        return ELF not in extract_col(col, row_min, row_max, grid)


def move_elf(grid, current_pos, new_pos) -> list[str]:
    row, col = current_pos
    new_row, new_col = new_pos

    # Remove the elf from the current pos and add it to the new pos
    grid[row] = grid[row][:col] + EMPTY_SPACE + grid[row][col + 1 :]
    grid[new_row] = grid[new_row][:new_col] + ELF + grid[new_row][new_col + 1 :]

    # print("Old pos: {}, new pos: {}".format(current_pos, new_pos))

    return grid


def count_empty_tiles(grid, elf_positions) -> int:
    rows, cols = zip(*elf_positions)  # Separates rows and cols into two tuples

    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    print("Minimum Row:", min_row)
    print("Maximum Row:", max_row)
    print("Minimum Column:", min_col)
    print("Maximum Column:", max_col)

    empty_tiles = 0

    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if grid[row][col] == EMPTY_SPACE:
                empty_tiles += 1

    return empty_tiles


max_rounds = 10
direction_order = [NORTH, SOUTH, WEST, EAST]
direction_changes = {
    NORTH: (-1, 0),  # UP
    EAST: (0, 1),  # RIGHT
    SOUTH: (1, 0),  # DOWN
    WEST: (0, -1),  # LEFT
}


def solve_task1():
    grid, elf_positions = read_input("test.txt")

    for round in range(max_rounds):
        proposed_moves = {}

        for pos in elf_positions:
            new_pos = get_proposed_move(round, pos, grid)

            # If no possible moves found, continue to next elf
            if new_pos is None:
                continue

            if new_pos not in proposed_moves:
                proposed_moves[new_pos] = [pos]
            else:
                proposed_moves[new_pos] += pos

        # Loop through all the proposed moves and perform the moves that only one elf proposed
        for new_pos, current_pos in proposed_moves.items():
            if len(current_pos) > 1:
                continue

            grid = move_elf(grid, current_pos[0], new_pos)
            elf_positions.remove(current_pos[0])
            elf_positions.add(new_pos)

        print("\nROUND {}".format(round))
        pprint(grid)

    empty_tiles = count_empty_tiles(grid, elf_positions)
    print("Answer: {}".format(empty_tiles))


solve_task1()
