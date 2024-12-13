from enum import IntEnum


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

OBSTACLE, EMPTY_SPACE = "#", "."
POSITIONS = {
    "^": Direction.NORTH, 
    ">": Direction.EAST, 
    "v": Direction.SOUTH, 
    "<": Direction.WEST
}
MOVE = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1),
}

def read_data(filename):
    with open(filename, "r") as f:
        obstacles = set()
        guard_pos = None

        lines = f.readlines()
        max_row = len(lines)
        max_col = len(lines[0])

        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                if ch in POSITIONS:
                    guard_pos = ((row, col), POSITIONS[ch])
                elif ch == OBSTACLE:
                    obstacles.add((row, col))

        return obstacles, tuple(guard_pos), max_row, max_col

def is_inside_grid(guard_pos, max_row, max_col):
    row, col = guard_pos[0]
    return 0 <= row < max_row and 0 <= col < max_col

def move(guard_pos, obstacles):
    current_pos, direction = guard_pos
    next_pos = (current_pos[0] + MOVE[direction][0], current_pos[1] + MOVE[direction][1])

    while next_pos in obstacles:
        direction = Direction((direction + 1) % 4)
        next_pos = (current_pos[0] + MOVE[direction][0], current_pos[1] + MOVE[direction][1])

    return (next_pos, direction)

def solve_p1():
    obstacles, guard_pos, max_row, max_col = read_data("input.txt")
    visited = set()

    while is_inside_grid(guard_pos, max_row, max_col):
        visited.add(guard_pos[0])
        guard_pos = move(guard_pos, obstacles)

    return len(visited)

def solve_p2():
    obstacles, guard_start_pos, max_row, max_col = read_data("input.txt")
    guard_path = set()
    visited_positions = set()
    added_obstacles = set()

    # Simulate guard's original path
    guard_pos = guard_start_pos
    while is_inside_grid(guard_pos, max_row, max_col):
        guard_path.add(guard_pos[0])
        guard_pos = move(guard_pos, obstacles)

    # Test placing obstacles
    for pos in guard_path:
        if pos == guard_start_pos[0]:  # Cannot place on starting position
            continue

        # Simulate with new obstacle
        new_obstacles = obstacles.union({pos})
        guard_pos = guard_start_pos
        visited_positions.clear()

        while is_inside_grid(guard_pos, max_row, max_col):
            if guard_pos in visited_positions:  # Loop detected
                added_obstacles.add(pos)
                break
            visited_positions.add(guard_pos)
            guard_pos = move(guard_pos, new_obstacles)

    return len(added_obstacles)


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
