import numpy as np

def read_input(filename):
    with open(filename) as f:
        data = f.read().strip().split("\n")

        n_rows = len(data)
        n_cols = len(data[0])

        data_matrix = np.zeros((n_rows, n_cols))
        result_matrix = np.full((n_rows, n_cols), False)

        for row in range(n_rows):
            for col in range(n_cols):
                data_matrix[row][col] = int(data[row][col])
            
        return data_matrix, result_matrix

def is_visible(row_pos, col_pos, full_row, full_col):
    # Check if tree is on the border
    if row_pos == 0 or row_pos == n_rows-1:
        return True
    
    if col_pos == 0 or col_pos == n_cols-1:
        return True

    tree_height = full_row[col_pos]

    # Check if taller than any other tree in the row. First from left, then from right.
    if tree_height > max(full_row[0:col_pos]): return True
    if tree_height > max(full_row[col_pos+1:]): return True
    
    # Then check columns. 
    if tree_height > max(full_col[0:row_pos]): return True
    if tree_height > max(full_col[row_pos+1:]): return True

    # If none of the check returned True -> Tree is not visible.
    return False

input, result = read_input("input.txt")
n_rows, n_cols = input.shape

for row in range(n_rows):
    for col in range(n_cols):        
        if is_visible(row, col, input[row,:], input[:,col]):
           result[row][col] = True

print(np.sum(result))

