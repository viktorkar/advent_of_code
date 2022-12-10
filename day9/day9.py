def read_input(filename):
    with open(filename) as f:
        data = f.read().strip().split("\n")
        data = [line.split(" ") for line in data]

    return data

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

def move_head(direction, pos):
    x,y = pos
    if direction == UP:
        return x, y+1
    elif direction == DOWN:
        return x, y-1
    elif direction == RIGHT:
        return x+1, y
    elif direction == LEFT:
        return x-1, y

def move_tail(head_pos, tail_pos):
    xh, yh = head_pos
    xt, yt = tail_pos

    x_delta = abs(xh-xt)
    y_delta = abs(yh-yt)

    if x_delta == 0: # Head and tail are on the same x-coordinate
        if y_delta == 2: # We need to move tail down or up
            yt = yt+1 if yt < yh else yt-1

    elif y_delta == 0: # Head and tail are on the same y-coordinate
        if x_delta == 2: # We need to move tail left or right
            xt = xt+1 if xt < xh else xt-1

    elif x_delta and y_delta != 1 or y_delta and x_delta != 1: # The tail and head are diagonal
        xt = xt+1 if xh > xt else xt-1
        yt = yt+1 if yh > yt else yt-1

    return xt, yt

def solve_task1():
    input = read_input("input.txt")
    visited_positions = set()
    xh, yh, xt, yt = 0, 0, 0, 0
    visited_positions.add((xt, yt))

    for line in input:
        direction, n_steps = line
        n_steps = int(n_steps)

        for i in range(n_steps):
            xh, yh = move_head(direction, (xh, yh))
            xt, yt = move_tail((xh, yh), (xt, yt))
            visited_positions.add((xt, yt))

    print("Task1 Solution: Number of visited positions =", len(visited_positions))

def solve_task2():
    input = read_input("input.txt")
    visited_positions = set()
    xh, yh = 0, 0
    knots = [(0,0) for _ in range(9)]
    visited_positions.add(knots[-1])

    for line in input:
        direction, n_steps = line
        n_steps = int(n_steps)

        for i in range(n_steps):
            xh, yh = move_head(direction, (xh, yh))
            knots[0] = move_tail((xh, yh), knots[0])
            for j in range(1, len(knots)):
                knots[j] = move_tail(knots[j-1], knots[j])

            visited_positions.add(knots[-1]) # The last knot is the tail

    print("Task2 Solution: Number of visited positions =", len(visited_positions))

solve_task1()
solve_task2()