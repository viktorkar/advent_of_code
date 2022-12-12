import numpy as np

##########################################################################################################################
def read_input(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

##########################################################################################################################
def get_distance(from_mountain, to_mountain):
    return ord(to_mountain) - ord(from_mountain)

##########################################################################################################################
def is_climbable(from_mountain, to_mountain):
    return get_distance(from_mountain, to_mountain) <= 1

##########################################################################################################################
def create_graph(input):
    graph = {}
    input_matrix = np.array([[*ch] for ch in input.split("\n")])
    n_rows, n_cols = input_matrix.shape

    # Extract start and stop IDs
    start_row, start_col = [x[0] for x in np.where(input_matrix == "S")]
    end_row, end_col = [x[0] for x in np.where(input_matrix == "E")]
    start_id = n_cols*start_row+start_col
    end_id = n_cols*end_row+end_col

    # Replace the start and end characters with their heights
    input_matrix= np.char.replace(input_matrix, 'S', 'a')
    input_matrix= np.char.replace(input_matrix, 'E', 'z')

    for row, line in enumerate(input_matrix):
        for col, current_mountain in enumerate(line):
            vertices = []
            current_mountain_id = n_cols*row+col

            if row != 0:
                mountain_up = input_matrix[row-1, col]
                if is_climbable(current_mountain, mountain_up):
                    mountain_up_id = n_cols*(row-1) + col
                    vertices.append(mountain_up_id)
            
            if row != n_rows-1:
                mountain_down = input_matrix[row+1, col]
                if is_climbable(current_mountain, mountain_down):
                    mountain_down_id = n_cols*(row+1) + col
                    vertices.append(mountain_down_id)

            if col != 0:
                mountain_left = input_matrix[row, col-1]
                if is_climbable(current_mountain, mountain_left):
                    mountain_left_id = n_cols*row+col-1
                    vertices.append(mountain_left_id)

            if col != n_cols-1:
                mountain_right = input_matrix[row, col+1]
                if is_climbable(current_mountain, mountain_right):
                    mountain_right_id = n_cols*row+col+1
                    vertices.append(mountain_right_id)

            graph[current_mountain_id] = [current_mountain, vertices]

    return graph, start_id, end_id

##########################################################################################################################
def find_shortest_path(graph, start_id, end_id):
    visited_mountains =  set()
    queue = []

    visited_mountains.add(start_id)
    queue.append((start_id, [start_id])) # (Node, [Path])

    
    while len(queue) > 0:
        (node, path) = queue.pop(0)
        height, mountains = graph[node]

        for mountain in mountains:
            if mountain not in visited_mountains:
                if mountain == end_id:
                    return path + [mountain]

                visited_mountains.add(mountain)
                queue.append((mountain, path + [mountain]))

##########################################################################################################################
def solve_task1():
    input = read_input("input.txt")
    graph, start_id, end_id = create_graph(input)
    shortest_path = find_shortest_path(graph, start_id, end_id)

    if shortest_path != None:
        print("Task1: Number of steps in shortest path:", len(shortest_path)-1)
    else:
        print("Task1: No path found")

##########################################################################################################################
def solve_task2():
    input = read_input("input.txt")
    graph, _, end_id = create_graph(input)
    min_dist = np.inf

    for node_id in graph:
        height, _ = graph[node_id]

        if height == 'a':
            path_to_end = find_shortest_path(graph, node_id, end_id)
            dist = len(path_to_end) - 1 if path_to_end else np.inf

            min_dist = min(min_dist, dist)

    if min_dist != np.inf:
        print("Task2: Number of steps in shortest path:", min_dist)
    else:
        print("Task2: No path found")


solve_task1()
solve_task2()
