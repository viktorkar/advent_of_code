import re

def read_input(filename):
    valves = {}
    with open(filename) as f:
        for line in f:
            data = re.findall(r"([A-Z]{2,}|\d+)", line)
            valve, flow, neighbours = data[0], int(data[1]), data[2:]
            valves[valve] = (flow, neighbours)

    return valves

def get_total_flow_of_valve(flow, timer):
    return flow*timer

def get_optimal_flow_of_neighbour(neighbours, valves, total_flow, timer, visited_valves):
    optimal_neighbour_flow = total_flow

    for valve in neighbours:
        # Loop through already not visisted neighbours
        if valve not in visited_valves:
            visited_valves.add(valve)
            valve_flow = find_max_flow(valves, valve, total_flow, timer-1, visited_valves) # Recursive call

            # Update the optimal flow
            optimal_neighbour_flow = max(optimal_neighbour_flow, valve_flow)

    return optimal_neighbour_flow

def find_max_flow(valves, current_valve, total_flow, timer, visited_valves):
    optimal_flow = total_flow

    # Stop criterium
    if timer == 0:
        return optimal_flow
    
    # Get the flow of the current valve and its neighbours
    flow, neighbours = valves[current_valve]

    # We have 2 choices:
    # 1. We open the valve and if we have time, go to another valve
    valve_flow = get_total_flow_of_valve(flow, timer-1)
    choice1 = get_optimal_flow_of_neighbour(neighbours, valves, total_flow+valve_flow, timer-2, visited_valves)

    # 2. We go to another valve without opening the current valve
    choice2 = get_optimal_flow_of_neighbour(neighbours, valves, total_flow, timer-1, visited_valves)

    optimal_flow = max(choice1, choice2)

    return optimal_flow


def solve_task1():
    valves = read_input("input.txt")
    timer = 30
    start_valve = "AA"
    visited_valves = set([start_valve])

    maximum_flow = find_max_flow(valves, start_valve, 0, timer, visited_valves)

    print("Solution Task 1: Maximum flow =", maximum_flow)



solve_task1()