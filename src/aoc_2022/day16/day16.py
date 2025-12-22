import re

###########################################################################
def read_input(filename):
    # First, create the graph and flows
    G, F = {}, {}
    with open(filename) as f:
        for line in f:
            data = re.findall(r"([A-Z]{2,}|\d+)", line)
            valve, flow, neighbours = data[0], int(data[1]), data[2:]
            G[valve] = neighbours

            if flow > 0:
                F[valve] = flow
    
    # Calculate the travel costs from all valves to all other valves.
    T = {from_valve: {to_valve: 1 if to_valve in G[from_valve] else float('+inf') for to_valve in G} for from_valve in G}
    for k in T:
        for i in T:
            for j in T:
                T[i][j] = min(T[i][j], T[i][k]+T[k][j])

    # Since we have very few interesting valves, we can use bits so represent if a valve has been visited
    I = {valve: 1<<i for i, valve in enumerate(F)}
    
    return G, F, T, I

G, F, T, I = read_input("input.txt")

##########################################################################
def find_possible_flows(current_valve, state, timer, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)

    for valve in F:
        # Subtract the number of steps to get from current_valve to valve and -1 to open it
        new_timer = timer - T[current_valve][valve] - 1

        # Stop criterium -> All valves visited or timer has run out 
        if I[valve] & state or new_timer <= 0:
            continue
        
        # Calculate the new flow
        new_flow = flow + F[valve] * new_timer

        # Recursive call
        find_possible_flows(valve, state | I[valve], new_timer, new_flow, answer)

    return answer

###################################################################################################
def solve_task1():
    timer = 30
    start_valve = "AA"
    start_state = 0
    start_flow = 0

    maximum_flow = max(find_possible_flows(start_valve, start_state, timer, start_flow, {}).values())

    print("Solution Task 1: Maximum flow =", maximum_flow)

###################################################################################################
def solve_task2():
    timer = 26
    start_valve = "AA"
    start_state = 0
    start_flow = 0

    flows = find_possible_flows(start_valve, start_state, timer, start_flow, {})
    maximum_flow = max(f1+f2 for s1, f1 in flows.items()
                             for s2, f2 in flows.items() if not s1 & s2) # Make sure the same valves haven't been opened

    print("Solution Task 2: Maximum flow =", maximum_flow)


solve_task1()
solve_task2()