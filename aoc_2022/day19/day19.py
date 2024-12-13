import re
import numpy as np
from heapq import heappush, heappop

robot_index = {"ore_robot": 0, "clay_robot": 1, "obsidian_robot": 2, "geode_robot": 3}
V = lambda *a: np.array()


def get_blueprints(filename):
    blueprints = []
    with open(filename) as f:
        for line in f:
            i, a, b, c, d, e, f = map(int, re.findall(r"\d+", line))
            blueprints.append(
                (V(0, 0, 0, a), V(0, 0, 0, 1)),  # Cost and production
                (V(0, 0, 0, b), V(0, 0, 1, 0)),  # of each robot type,
                (V(0, 0, d, c), V(0, 1, 0, 0)),  # in the order geode,
                (V(0, f, 0, e), V(1, 0, 0, 0)),  # obs, clay, and ore.
                (V(0, 0, 0, 0), V(0, 0, 0, 0)),  # Construct no robot.
            )

    return blueprints


def can_build_robot(robot_costs, resources):
    has_ore = robot_costs["ore"] <= resources[0]
    has_clay = robot_costs["clay"] <= resources[1]
    has_obsidian = robot_costs["obsidian"] <= resources[2]

    return has_ore and has_clay and has_obsidian


def get_buildable_robots(blueprint, resources):
    buildable_robots = [None]  # Representing not doing anything

    for robot_type in blueprint:
        if can_build_robot(blueprint[robot_type], resources):
            buildable_robots.append(robot_type)

    print(buildable_robots)
    return buildable_robots


def build_robot(robot_type, robots, resources, blueprint):
    costs = blueprint[robot_type]
    new_robots, new_resources = robots.copy(), resources.copy()
    new_resources[0] -= costs["ore"]
    new_resources[1] -= costs["clay"]
    new_resources[2] -= costs["obsidian"]

    new_robots[robot_index[robot_type]] += 1

    return new_robots, new_resources


def temp(passed_time, robots, resources, blueprint):
    # If 24 minutes passed, return number of mined geodes
    if passed_time == 24:
        return resources[3]

    max_mined_geodes = 0

    for robot_type in get_buildable_robots(blueprint, resources):
        if robot_type is not None:
            new_robots, new_resources = build_robot(robot_type, robots, resources, blueprint)
        else:
            new_robots, new_resources = robots.copy(), resources.copy()

        new_resources = [x + y for x, y in zip(new_resources, robots)]
        new_time = passed_time + 1

        mined_geodes = temp(new_time, new_robots, new_resources, blueprint)
        max_mined_geodes = max(mined_geodes, max_mined_geodes)

    return max_mined_geodes


def calculate_quality_level(blueprint):
    initial_robots = [1, 0, 0, 0]  # 1 ore robot, 0 clay robot, 0 obsidian robot, 0 geode robot
    initial_resources = [0, 0, 0, 0]  # 0 ore, 0 clay, 0 obsidan, 0 geode

    return temp(0, initial_robots, initial_resources, blueprint)


def solve_task1():
    blueprints = get_blueprints("input.txt")
    quality_level_sum = 0

    for id in blueprints:
        blueprint = blueprints[id]
        quality_level_sum += calculate_quality_level(blueprint) * id
        break

    return quality_level_sum


def main():
    print("Answer task 1: {}".format(solve_task1()))


if __name__ == "__main__":
    main()
