def read_input(filename):
    with open(filename) as f:
        data = f.read().strip().split("\n")
        data = [line for line in data if line] # removes all empty lines
        return list(map(eval, data))

##########################################################################################################################
def compare(packet1, packet2):
    packet1_is_list = isinstance(packet1, list)
    packet2_is_list = isinstance(packet2, list)

    if packet1_is_list and packet2_is_list:
        return compare_lists(packet1, packet2)
    elif packet2_is_list and not packet1_is_list:
        return compare_lists([packet1], packet2)
    elif packet1_is_list and not packet2_is_list:
        return compare_lists(packet1, [packet2])
    else:
        return compare_numbers(packet1, packet2)

##########################################################################################################################
def compare_lists(packet1, packet2):
    length_p1 = len(packet1)
    length_p2 = len(packet2)
    longest_packet = max(length_p1, length_p2)
    
    for i in range(longest_packet):
        if length_p1 == i: # Packet 1 ran out of items -> correct
            return True

        if length_p2 == i: # Packet 2 ran out of items -> incorrect
            return False

        result = compare(packet1[i], packet2[i]) # Recursive call with next items

        # Check if we can return a result, else continue
        if result is not None:
            return result
 
    # If we reach here -> no decision has been taken
    return None

##########################################################################################################################
def compare_numbers(number1, number2):
    if number1 == number2:
        return None

    return number1 < number2

##########################################################################################################################
def sort_packets(packets):
    num_packets = len(packets)

    for i in range(num_packets):
        for j in range(0, num_packets - i - 1):
            result = compare(packets[j], packets[j + 1])

            # If packets are not in order -> switch positions
            if result == False: 
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    return packets

##########################################################################################################################
def solve_task1():
    input = read_input("input.txt")
    n_lines = len(input)
    correct_packets = []
    pair_idx = 1

    for i in range(0, n_lines, 2):
        
        packet1 = input[i]
        packet2 = input[i+1]

        if compare(packet1, packet2):
            correct_packets.append(pair_idx)

        pair_idx +=1

    print("There are {} correctly ordered messages".format(len(correct_packets)))
    print("Sum of packet indexes:", sum(correct_packets))

##########################################################################################################################
def solve_task2():
    divider1 = [6]
    divider2 = [2]
    input = read_input("input.txt")
    input += [divider1, divider2]

    sorted_input = sort_packets(input)
    answer = (sorted_input.index(divider1) + 1) * (sorted_input.index(divider2) + 1)

    print("Task2 solution:", answer)

solve_task1()
solve_task2()