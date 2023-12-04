import re

##############################################################################################
def manhattan_distance(point1, point2):
  x1, y1 = point1
  x2, y2 = point2
  return abs(x1 - x2) + abs(y1 - y2)

##############################################################################################
def read_input(filename):
    sensors, beacons = set(), set()

    with open(filename) as f:
        for line in f:
            coordinates = [int(number) for number in re.findall(r'\d+', line)]
            sensor_x, sensor_y = coordinates[:2]
            beacon_x, beacon_y = coordinates[2:]
            distance = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))

            sensors.add((sensor_x, sensor_y, distance))
            beacons.add((beacon_x, beacon_y))

    return sensors, beacons

##############################################################################################
def is_covered_by_sensor(point, sensors, beacons):
    for sx, sy, d in sensors:
        dist = manhattan_distance(point, (sx, sy))

        if dist <= d and point not in beacons:
            return True

    return False

##############################################################################################
def solve_task1():
    sensors, beacons = read_input("input.txt")
    min_x = min(x-d for x, _, d in sensors)
    max_x = max(x+d for x,_,d in sensors)
    counter = 0
    y = 2_000_000

    # Loop through all the points in the row and check if any of the sensors conver that point.
    for x in range(min_x, max_x):
        if is_covered_by_sensor((x,y), sensors, beacons):
            counter += 1

    print("Solution Task1: There are {} positions that cannot contain a beacon".format(counter))

solve_task1()