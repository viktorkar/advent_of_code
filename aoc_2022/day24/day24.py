from time import time
import numpy as np
import math
from functools import reduce
from heapq import heappush, heappop


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
    with open(filename) as f:
        return f.read().splitlines()


def get_states(data):
    n_rows, n_cols = len(data) - 2, len(data[0]) - 2

    # Create a 2D list for each type of wind and for 'empty' spots
    north_winds, south_winds, west_winds, east_winds, empty_spots = [
        np.zeros((n_rows, n_cols), dtype=bool) for _ in range(5)
    ]

    # Put the lists in a map mapped to their wind type
    wind_map = {
        "^": north_winds,
        "v": south_winds,
        "<": west_winds,
        ">": east_winds,
        ".": empty_spots,
    }

    # Fill out the 2D lists with the initial wind positions
    for row, line in enumerate(data[1:-1]):
        for col, char in enumerate(line[1:-1]):
            wind_map[char][row, col] = True

    del empty_spots  # We don't need the store the empty spots

    # Create the first and last line (where start and finish is)
    first_line = np.ones((1, n_cols), dtype=bool)
    first_line[0, 0] = False

    end_line = np.ones((1, n_cols), dtype=bool)
    end_line[0, -1] = False

    # Create all possible states
    states = []
    for _ in range(math.lcm(n_rows, n_cols)):
        blizzard_state = reduce(np.logical_or, [north_winds, south_winds, west_winds, east_winds])
        states.append(np.vstack([first_line, blizzard_state, end_line]))

        # Update the position of the winds by shifting top/bottom rows/columns
        north_winds = np.vstack([north_winds[1:], north_winds[:1]])
        south_winds = np.vstack([south_winds[-1:], south_winds[:-1]])
        west_winds = np.hstack([west_winds[:, 1:], west_winds[:, :1]])
        east_winds = np.hstack([east_winds[:, -1:], east_winds[:, :-1]])

    return states


def get_open_positions(player_pos, state):
    possible_positions = []
    r0, c0 = player_pos
    max_row, max_col = state.shape

    for row, col in [(r0, c0), (r0 + 1, c0), (r0 - 1, c0), (r0, c0 + 1), (r0, c0 - 1)]:
        if row < 0 or col < 0 or row >= max_row or col >= max_col:
            continue

        if not state[row, col]:
            possible_positions.append((row, col))

    return possible_positions


def dijkstra(states, start_pos, end_pos, initial_state):
    n_states = len(states)
    queue = []

    visited = {(start_pos, initial_state): 0}
    heappush(queue, (0, start_pos, initial_state))

    while queue:
        (time, player_pos, state) = heappop(queue)

        # Stop criterium
        if player_pos == end_pos:
            return time

        next_state = (state + 1) % n_states
        next_time = time + 1

        for next_pos in get_open_positions(player_pos, states[next_state]):
            v = visited.get((next_pos, next_state))

            if v is None or v > next_time:
                visited[(next_pos, next_state)] = next_time
                heappush(queue, (next_time, next_pos, next_state))


@timer_func
def solve_task1(filename):
    data = read_input(filename)
    states = get_states(data)

    n_rows, n_cols = states[0].shape
    end_pos = (n_rows - 1, n_cols - 1)

    return dijkstra(states, (0, 0), end_pos, 0)


@timer_func
def solve_task2(filename):
    data = read_input(filename)
    states = get_states(data)
    n_states = len(states)

    n_rows, n_cols = states[0].shape
    start_pos = (0, 0)
    end_pos = (n_rows - 1, n_cols - 1)

    t1 = dijkstra(states, start_pos, end_pos, 0)
    t2 = dijkstra(states, end_pos, start_pos, t1 % n_states)
    t3 = dijkstra(states, start_pos, end_pos, (t1 + t2) % n_states)

    return sum([t1, t2, t3])


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve_task1("input.txt")))
    print("Answer Task 2: {}".format(solve_task2("input.txt")))
