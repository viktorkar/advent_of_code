decryption_key = 811589153

def get_input(filename, task):
    id_map = {}
    id_zero = 0
    multiplier = 1 if task == 1 else decryption_key

    with open(filename) as f:
        for unique_id, number in enumerate(f.readlines()):
            id_map[unique_id] = int(number) * multiplier

            id_zero = unique_id if int(number) == 0 else id_zero # Save which id that 0 is assigned

    return id_map, id_zero

def solve(task):
    id_map, id_zero = get_input("input.txt", task)
    mixed = list(id_map.keys())
    n = len(mixed) - 1 # -1 since one item will be in motion, think that the item is first 'deleted' from the list
    rounds = 1 if task == 1 else 10

    for _ in range(rounds):
        for id, value in id_map.items():
            old_index = mixed.index(id)
            new_index = (old_index + value + n) % n
            
            del mixed[old_index]
            mixed.insert(new_index, id)

    index_zero = mixed.index(id_zero)
    indexes = [(index_zero + x) % len(id_map) for x in [1000, 2000, 3000]]
    ids = [mixed[index] for index in indexes]
    numbers = [id_map[x] for x in ids]

    print(sum(numbers))

solve(task=1)
solve(task=2)


