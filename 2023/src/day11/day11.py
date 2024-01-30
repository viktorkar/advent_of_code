from itertools import combinations

def get_data():
    with open("input.txt", "r") as f:
        return [list(line) for line in f.read().splitlines()]


def expand_universe(universe):
    m, n = len(universe), len(universe[0])

    i = 0
    while i < len(universe):
        if "#" not in universe[i]:
            universe.insert(i, ["."] * n)
            m += 1
            i += 2
        else:
            i += 1

    j = 0
    while j < len(universe[0]):
        if "#" not in [universe[i][j] for i in range(m)]:
            for i in range(m):
                universe[i].insert(j, ".")
            n += 1
            j += 2
        else:
            j += 1

    return universe


def get_galaxies(universe):
    m, n = len(universe), len(universe[0])
    return [(i, j) for i in range(m) for j in range(n) if universe[i][j] == "#"]


def calculate_distances(galaxies):
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        total += abs(x1 - x2) + abs(y1 - y2)

    return total


def solve():
    universe = get_data()
    universe = expand_universe(universe)
    galaxies = get_galaxies(universe)

    return calculate_distances(galaxies)


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve()))
