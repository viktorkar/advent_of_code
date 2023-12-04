with open("input.txt") as f:
    calories = []
    counter = 0
    for line in f:
        line = line.strip()

        if (line == ""):
            calories.append(counter)
            counter = 0
        else:
            counter += int(line)

    print(max(calories))

    print(sum(sorted(calories, reverse=True)[0:3]))

