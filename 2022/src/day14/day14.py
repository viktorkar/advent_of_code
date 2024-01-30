def get_rock_coordinates(filename):
    rock_coordinates = set()
    rock_bottom = 0
    with open(filename) as f:
        for line in f:
            coordinates = line.split(" -> ")

            for c in range(len(coordinates)-1):
                # Extract the coordinates and conver to int
                x1, y1 = [int(xy) for xy in coordinates[c].split(",")]
                x2, y2 = [int(xy) for xy in coordinates[c+1].split(",")]

                # To make life easier, sort coordinates to always have the lowest first
                x1, x2 = sorted([x1, x2])
                y1, y2 = sorted([y1, y2])

                # Check if we have vertical (x1 == x2) or horizontal rocks (y1 == y2)
                if x1 == x2:
                    rock_coordinates.update([(x1, y) for y in range(y1, y2+1)])
                elif y1 == y2:
                    rock_coordinates.update([(x, y1) for x in range(x1, x2+1)])

                rock_bottom = max(rock_bottom, y1, y2)

    return rock_coordinates, rock_bottom

##################################################################################################
def solve_task1():
    obstacles, rock_bottom = get_rock_coordinates("input.txt")
    sand_origin = (500, 0)
    sand_counter = 0

    while True:
        sand_x, sand_y = sand_origin
        sand_counter += 1

        while True:
            # Stop Criteria
            if sand_y > rock_bottom or (sand_x, sand_y) in obstacles:
                return sand_counter-1

            # First try to drop straight down
            elif not (sand_x, sand_y+1) in obstacles:
                sand_y += 1
            # Then try to drop left
            elif not (sand_x-1, sand_y+1) in obstacles:
                sand_x -= 1
                sand_y += 1
            # Then try to drop right
            elif not (sand_x+1, sand_y+1) in obstacles:
                sand_x += 1
                sand_y += 1
            # If we can't drop more -> add current pos to obstacles and break from inner loop
            else:
                obstacles.add((sand_x, sand_y))
                break

##################################################################################################
def solve_task2():
    obstacles, rock_bottom = get_rock_coordinates("input.txt")
    new_rock_bottom = rock_bottom + 2 
    sand_origin = (500, 0)
    sand_counter = 0

    while True:
        sand_x, sand_y = sand_origin
        sand_counter += 1

        while True:
            # Specific case,
            if sand_y+1 == new_rock_bottom:
                obstacles.add((sand_x, sand_y))
                break

            # Stop Criterium
            if (sand_x, sand_y) in obstacles:
                return sand_counter-1
            
            # First try to drop straight down
            elif not (sand_x, sand_y+1) in obstacles:
                sand_y += 1
            # Then try to drop left
            elif not (sand_x-1, sand_y+1) in obstacles:
                sand_x -= 1
                sand_y += 1
            # Then try to drop right
            elif not (sand_x+1, sand_y+1) in obstacles:
                sand_x += 1
                sand_y += 1
            # If we can't drop more -> add current pos to obstacles and break from inner loop
            else:
                obstacles.add((sand_x, sand_y))
                break

print("Task1 solution:", solve_task1())
print("Task2 solution:", solve_task2())

