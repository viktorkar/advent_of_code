UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

move = {UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0)}

pipe_direction = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [DOWN, LEFT],
    "F": [DOWN, RIGHT],
    "S": [UP, DOWN, LEFT, RIGHT],
    ".": [],
}

counter_direction = {UP: DOWN, LEFT: RIGHT, DOWN: UP, RIGHT: LEFT}


def get_data():
    with open("input.txt") as f:
        graph = {}
        start = (0, 0)
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                graph[(col, row)] = c

                if c == "S":
                    start = (col, row)

    return graph, start


def get_next_positions(current_pos, graph):
    result = []
    current_pipe = graph[current_pos]
    directions = pipe_direction[current_pipe]

    for direction in directions:
        new_pos = tuple(map(lambda i, j: i + j, current_pos, move[direction]))
        next_pipe = graph[new_pos]

        if is_connected(next_pipe, direction):
            result.append(new_pos)

    return result


def is_connected(next_pipe, direction):
    return counter_direction[direction] in pipe_direction[next_pipe]


def dfs(visited, queue, graph):
    steps = -1

    while queue:
        next_positions = set()
        for pos in queue:
            for next_pos in get_next_positions(pos, graph):
                if next_pos not in visited:
                    visited.add(next_pos)
                    next_positions.add(next_pos)

        queue = next_positions
        steps += 1

    return steps

def solve():
    graph, start_pos = get_data()
    visited = set()
    queue = set()

    visited.add(start_pos)
    queue.add(start_pos)

    return dfs(visited, queue, graph)

if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve()))
