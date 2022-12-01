# Need minimum 50 stars by december 25th
# 

# Task 1
def find_max_calories(filename):
    maxCalories = 0
    currentCalories = 0

    with open(filename) as f:
        for line in f:
            # If line is empty -> We will be parsing a new elf
            if (not line.strip()):
                if currentCalories > maxCalories:
                    maxCalories = currentCalories

                currentCalories = 0
            else:
                currentCalories += int(line)
    
    print("Task 1: Max calories =", maxCalories)


# Task 2
def find_total_calories(n, filename):
    totals = []
    currentCalories = 0

    with open(filename) as f:
        # Load the data
        for line in f:
            # If line is empty -> We will be parsing a new elf
            if (not line.strip()):
                totals.append(currentCalories)
                currentCalories = 0
            else:
                currentCalories += int(line)
        
        # Sort the data
        totals.sort(reverse=True)
        
        # Print the sum of the top n
        result = sum(totals[:n])
        print("Task 2: Total calories of the top %i elfs = %i" % (n, result))


find_max_calories("input.txt")
find_total_calories(3, "input.txt")