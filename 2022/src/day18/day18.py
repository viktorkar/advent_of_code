import collections


def read_input(filename):
    with open(filename) as f:
        return set(tuple(map(int, x.split(','))) for x in f.read().splitlines())
    

def neighbors(x, y, z):
    yield from ((x+1, y, z), (x, y+1, z), (x, y, z+1))
    yield from ((x-1, y, z), (x, y-1, z), (x, y, z-1))


cubes = read_input("input.txt")
mins, maxs = [min(x)-1 for x in zip(*cubes)], [max(x)+1 for x in zip(*cubes)]

# Task 1
total1 = sum(n not in cubes for c in cubes for n in neighbors(*c))
print("Solution to part 1: Number of visable surfaces:", total1)

# Task2
total2 = 0
Q, visited = collections.deque([tuple(mins)]), set(cubes)

while len(Q):
    for cube in neighbors(*Q.popleft()):
        if not all(a <= x <= b for a, b, x in zip(mins, maxs, cube)): 
            continue

        total2 += cube in cubes

        if cube in visited: 
            continue

        visited.add(cube)
        Q.append(cube)

print("Solution to part 2: Number of visable surfaces:", total2)

