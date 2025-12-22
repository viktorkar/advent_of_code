
items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_item_priority(item):
    return items.find(item) + 1

##########################################################################################################
def find_common_item(rucksack_items):
    number_of_items = len(rucksack_items)
    middle_index = int(number_of_items / 2)

    items_comp1 = rucksack_items[:middle_index]
    items_comp2 = rucksack_items[middle_index:]
    common_items = list(set(items_comp1) & set(items_comp2))

    return common_items[0]

##########################################################################################################
def solve_task1(filename):
    total_priority_score = 0

    with open(filename) as f:
        for line in f:
            rucksack_items = line.strip()
            common_item = find_common_item(rucksack_items)

            if common_item:
                total_priority_score += get_item_priority(common_item)

    print("Task1: Total priority score:", total_priority_score)

##########################################################################################################
def find_badge(group_items):
    common_items = list(set.intersection(*map(set, group_items)))

    return common_items[0]

##########################################################################################################
def solve_task2(filename):
    total_priority_score = 0

    with open(filename) as f:
        group_items = []

        for line in f:
            rucksack_items = line.strip()
            group_items.append(rucksack_items)

            # If we have parsed all backbacks of the group -> find the badge (common item) and reset the list.
            if len(group_items) == 3:
                common_item = find_badge(group_items)
                total_priority_score += get_item_priority(common_item)
                group_items = []

    print("Task2: Total priority score:", total_priority_score)



solve_task1("input.txt")
solve_task2("input.txt")