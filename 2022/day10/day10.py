import numpy as np

###############################################################################################
def solve_task1():
    x = 1
    cycle = 0
    index_markers = [20, 60, 100, 140, 180, 220]
    saved_x_values = []

    with open("input.txt") as f:
        for line in f:
            op = line.strip().split(" ")
            exc_time = 1 if op[0] == "noop" else 2
            value = 0 if op[0] == "noop" else int(op[1])

            for i in range(exc_time):
                cycle += 1

                if (cycle in index_markers):
                    print("X at cycle {} == {}:".format(cycle, x))
                    saved_x_values.append(cycle*x)

            x += value
            
    print("Sum of x values=", sum(saved_x_values))

###############################################################################################
def solve_task2():
    cycle = 0
    row_index = 0
    sprite_position = 1 # x

    screen_width, screen_height = 40, 6
    screen = np.full((screen_height), "." * screen_width)
    print("Starting Screen:\n", screen)

    with open("input.txt") as f:
        for line in f:
            op = line.strip().split(" ")
            exc_time = 1 if op[0] == "noop" else 2
            value = 0 if op[0] == "noop" else int(op[1])

            for i in range(exc_time):
                pixel_index = cycle % screen_width
                cycle += 1

                if cycle % (screen_width+1) == 0:
                    row_index += 1

                pixel =  "#" if pixel_index in [sprite_position+i for i in range(-1, 2)] else "."

                # Edit pixel at correct pos. Strings are immutable to we have to do it this way?? bah
                pixel_row = screen[row_index]
                pixel_row = list(pixel_row)
                pixel_row[pixel_index] = pixel
                pixel_row = ''.join(pixel_row)
                screen[row_index] = pixel_row
                    
            sprite_position += value
                
    print("Resulting Screen:\n", screen)

solve_task1()
solve_task2()