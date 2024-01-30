def read_input(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    
    return data

################################################################################################
def check_unique(characters):
    n_chars = len(characters)
    for i in range(n_chars):
        char1 = characters[i]
        for j in range(i+1, n_chars):
            char2 = characters[j]
            if char1 == char2:
                return False
    return True

################################################################################################
def find_marker(message, n):
   for i in range(0, len(message)-n-1):
    characters = message[i:i+n]
    if check_unique(characters):
        print("Found unique characters: %s. Start of packet index: %i" % (characters, i+n))

        return i

################################################################################################
def solve_task1():
    message = read_input("input.txt")
    marker = find_marker(message, 4)

################################################################################################
def solve_task2():
    message = read_input("input.txt")
    marker = find_marker(message, 14)


solve_task1()
solve_task2()