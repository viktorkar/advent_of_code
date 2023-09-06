from time import time

WAIT = "wait"
GO_RIGHT = ">"
GO_LEFT = "<"
GO_UP = "^"
GO_DOWN = "v"

active_actions = [GO_RIGHT, GO_LEFT, GO_UP, GO_DOWN]

movement_changes = {
    WAIT: (0, 0),
    GO_UP: (-1, 0),  # UP
    GO_RIGHT: (0, 1),  # RIGHT
    GO_DOWN: (1, 0),  # DOWN
    GO_LEFT: (0, -1),  # LEFT
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


def read_input(filename) -> tuple[dict, tuple, tuple, tuple]:
    winds = {}

    with open(filename) as f:
        grid = f.read().splitlines()
        start_pos = (0, 0)
        end_pos = (0, 0)
        size = (len(grid) - 1, len(grid[0]) - 1)

        for row, line in enumerate(grid):
            for col, ch in enumerate(line):
                if ch != "#" and ch != ".":
                    winds[(row, col)] = [ch]

                if row == 0 and ch == ".":
                    start_pos = (row, col)

                if row == len(grid) - 1 and ch == ".":
                    end_pos = (row, col)

        return winds, start_pos, end_pos, size


def update_winds(winds):
    updated_winds = {}
    for wind_pos, wind_types in winds.items():
        for wind_type in wind_types:
            new_pos = move(wind_pos, wind_type)
            new_pos = new_pos[0] % max_row, new_pos[1] % max_col

            updated_winds.setdefault(new_pos, []).append(wind_type)

    return updated_winds


def is_inside_map(pos):
    row, col = pos
    return row > 0 and row < max_row and col > 0 and col < max_col


def get_possible_actions(winds, player_pos):
    possible_actions = [WAIT]

    for action in active_actions:
        new_pos = move(player_pos, action)

        # Check if new_pos inside map and there are not winds there
        if is_inside_map(new_pos) and new_pos not in winds:
            possible_actions.append(action)

    return possible_actions


def move(player_pos, action):
    row_change, col_change = movement_changes[action]
    player_pos = player_pos[0] + row_change, player_pos[1] + col_change

    return player_pos


def run(winds, player_pos, end_pos, n_actions):
    queue = [(winds, player_pos, n_actions)]
    visited = {(player_pos, n_actions): n_actions}

    while queue:
        (winds, player_pos, n_actions) = queue.pop()

        # Stop criterium
        if player_pos == end_pos:
            return n_actions

        winds = update_winds(winds)
        possible_actions = get_possible_actions(winds, player_pos)

        for action in possible_actions:
            next_pos = move(player_pos, action)
            n_actions += 1

            v = visited.get((next_pos, n_actions))

            if v is None or v > n_actions:
                visited[(next_pos, n_actions)] = n_actions
                queue.append((winds, next_pos, n_actions))


max_row, max_col = (0, 0)


@timer_func
def main(filename):
    global max_row, max_col

    winds, start_pos, end_pos, size = read_input(filename)
    max_row, max_col = size

    return run(winds, start_pos, end_pos, 0)


if __name__ == "__main__":
    print("Answer Task 1: {}".format(main("input.txt")))
