import re

def read_input(filename):
    valves = {}
    with open(filename) as f:
        for line in f:
            data = re.findall(r"([A-Z]{2,}|\d+)", line)
            valve, flow, neighbours = data[0], int(data[1]), data[2:]
            valves[valve] = (flow, neighbours)

    return valves

lines = [re.split('[\\s=;,]+', x) for x in open("input.txt").read().splitlines()]
G = {x[1]: set(x[10:]) for x in lines}
F = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
I = {x: 1<<i for i, x in enumerate(F)}
T = {x: {y: 1 if y in G[x] else float('+inf') for y in G} for x in G}
for k in T:
    for i in T:
        for j in T:
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])

def find_max_flow(current_valve, state, timer, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)

    for valve in F:
        # Subtract the number of steps to get from current_valve to valve,
        new_timer = timer - T[current_valve][valve] - 1

        # Stop criterium -> All valves visited or timer has run out 
        if I[valve] & state or new_timer <= 0:
            continue
        
        # Calculate the new flow
        new_flow = flow + F[valve] * new_timer

        # Recursive call
        find_max_flow(valve, state | I[valve], new_timer, new_flow, answer)

    return answer


def solve_task1():
    timer = 30
    start_valve = "AA"

    maximum_flow = max(find_max_flow(start_valve, 0, timer, 0, {}).values())

    print("Solution Task 1: Maximum flow =", maximum_flow)


solve_task1()


#print(G) # graph
#print(F) # flows where flow > 0
#print(I) # Each valve with flow > 0 connected to a value
#print(T) # Transition graph? Number of steps to each node from anywhere in the graph.