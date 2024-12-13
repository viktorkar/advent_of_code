from time import time

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
ELF = "#"
EMPTY_SPACE = "."

direction_order = [NORTH, SOUTH, WEST, EAST]
direction_changes = {
    NORTH: (-1, 0),  # UP
    EAST: (0, 1),  # RIGHT
    SOUTH: (1, 0),  # DOWN
    WEST: (0, -1),  # LEFT
}


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        return result

    return wrap_func


def read_input(filename) -> tuple[list[str], set]:
    elf_positions = set()

    with open(filename) as f:
        grid = f.read().splitlines()

        for row, line in enumerate(grid):
            for col, ch in enumerate(line):
                if ch == ELF:
                    elf_positions.add((row, col))

        return elf_positions


def get_proposed_move(round, current_pos, elf_positions) -> tuple[int, int]:
    n_directions = len(direction_order)

    for i in range(n_directions):
        index = ((round % n_directions) + i) % n_directions
        direction = direction_order[index]
        row_change, col_change = direction_changes[direction]
        new_pos = current_pos[0] + row_change, current_pos[1] + col_change

        # Return the proposed move if it is possible to move there
        if not is_blocked(new_pos, direction, elf_positions):
            return new_pos

    return None


def get_surrounding_points(pos):
    row, col = pos
    neighbors = []

    # Define the relative offsets for the surrounding points
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    neighbors = [(row + offset_row, col + offset_col) for offset_row, offset_col in offsets]

    return neighbors


def stay(current_pos, elf_positions) -> bool:
    for point in get_surrounding_points(current_pos):
        if point in elf_positions:
            return False

    return True


def is_blocked(new_pos, direction, elf_positions) -> bool:
    row, col = new_pos

    # Check that we are not blocked by any elves in that direction
    if direction == NORTH or direction == SOUTH:
        for x in range(col - 1, col + 2):
            if (row, x) in elf_positions:
                return True
        return False
    else:
        for x in range(row - 1, row + 2):
            if (x, col) in elf_positions:
                return True
        return False


def count_empty_tiles(elf_positions) -> int:
    rows, cols = zip(*elf_positions)  # Separates rows and cols into two tuples

    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    empty_tiles = (max_row - min_row + 1) * (max_col - min_col + 1) - len(elf_positions)

    return empty_tiles


@timer_func
def main(input_file, task2=False):
    elf_positions = read_input(input_file)
    n_rounds = 5000 if task2 else 10

    for round in range(n_rounds):
        proposed_moves = {}

        for pos in elf_positions:
            if stay(pos, elf_positions):
                continue

            new_pos = get_proposed_move(round, pos, elf_positions)

            # If no possible moves found, continue to next elf
            if new_pos is None:
                continue

            if new_pos not in proposed_moves:
                proposed_moves[new_pos] = [pos]
            else:
                proposed_moves[new_pos].append(pos)

        # Loop through all the proposed moves and perform the moves that only one elf proposed
        no_elves_moved = True
        for new_pos, current_pos in proposed_moves.items():
            if len(current_pos) > 1:
                continue

            elf_positions.remove(current_pos[0])
            elf_positions.add(new_pos)
            no_elves_moved = False

        if task2 and no_elves_moved:
            return round + 1

    if task2:
        print(
            "Error: The round where no elves moves was not found, increase maximum number of rounds."
        )
        return None
    else:
        return count_empty_tiles(elf_positions)


if __name__ == "__main__":
    assert main("test.txt") == 110
    assert main("test.txt", True) == 20

    print("Answer Task 1: {}".format(main("input.txt")))
    print("Answer Task 2: {}".format(main("input.txt", True)))
