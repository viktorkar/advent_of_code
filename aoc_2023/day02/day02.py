from time import time

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14
TOTAL_CUBES = RED_CUBES + GREEN_CUBES + BLUE_CUBES

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


def get_input(file_path):
    games = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into Game number and the list of values
            game_number, values_str = line.split(':')
            game_number = int(game_number.split(" ")[1])

            # Split the values into individual games
            game_values = [game.strip() for game in values_str.split(';')]

            # Convert each game string into a list of dictionaries with color counts
            game_data = []
            for game_str in game_values:
                color_counts = {}
                for item in game_str.split(','):
                    count, color = item.strip().split()
                    color_counts[color] = int(count)
                game_data.append(color_counts)

            # Store the data in the dictionary
            games[game_number] = game_data

    return games



def is_game_possible(game):
    for set in game:
      if set.get('blue', 0) > BLUE_CUBES or set.get('red', 0) > RED_CUBES or set.get('green', 0) > GREEN_CUBES:
          return False  

    return True

def get_power_minimum_set_of_cubes(game):
    max_red = 0
    max_blue = 0
    max_green = 0

    for set in game:
      max_red = max(max_red, set.get('red', 0))
      max_blue = max(max_blue, set.get('blue', 0))
      max_green = max(max_green, set.get('green', 0))

    return max_red * max_blue * max_green


@timer_func
def part1():
    games = get_input("input.txt")
    sum_of_ids = 0
    for game_id in games:
        if is_game_possible(games[game_id]):
            sum_of_ids += game_id
    

    return sum_of_ids

@timer_func
def part2():
    games = get_input("input.txt")
    sum = 0
    for game_id in games:
        sum += get_power_minimum_set_of_cubes(games[game_id])

    return sum


if __name__ == "__main__":
    print("Answer Task 1: {}".format(part1()))
    print("Answer Task 2: {}".format(part2()))
