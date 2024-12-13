def read_data(filename):
    with open(filename, "r") as file:
        rules_input, updates_input = map(str.splitlines, file.read().split("\n\n"))

    rules = {}
    for left, right in (rule.split("|") for rule in rules_input):
        left, right = int(left), int(right)
        rules.setdefault(left, set()).add(right)

    updates = [list(map(int, update.split(","))) for update in updates_input]
    return rules, updates

def is_valid_update(update, rules):
    n = len(update)
    return all(all(num in rules[update[i]] for num in update[i+1:]) for i in range(n))

def get_invalid_updates(rules, updates):
    invalid_updates = []
    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)

    return invalid_updates

def solve_p1():
    rules, updates = read_data("input.txt")
    return sum(update[len(update) // 2] for update in updates if is_valid_update(update, rules))


def solve_p2():
    rules, updates = read_data("input.txt")
    total = 0
    invalid_updates = get_invalid_updates(rules, updates)

    for update in invalid_updates:
        update_set = set(update)
        update.sort(key=lambda x: len(update_set.intersection(rules[x])), reverse=True)
        total += update[len(update) // 2]

    return total

if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
