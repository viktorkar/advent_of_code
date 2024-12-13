import sys
import math
import random
import time

money = 100
start = money


def roll_dice():
    return random.randrange(1,7)

def gamble(amount):
    global money
    print("Datorn kastar tärningen...")
    time.sleep(1)
    computer_roll = roll_dice()
    print("Numret blev:", computer_roll)
    time.sleep(1)

    print("Du kastar tärningen...")
    time.sleep(1)
    my_roll = roll_dice()
    print("Du fick: {}!".format(my_roll))
    time.sleep(1)

    if my_roll > computer_roll:
        print("Du vann: {} kr".format(amount))
        money += amount
    else:
        print("Du förlorade... :(")
        money -= amount

def get_amount():
    while True:
        inp = input()

        if not str.isdigit(inp):
            print("Du måste skriva in en siffra")
            continue
        

        amount = int(inp)
        if amount <= 0:
            print("Du måste satsa mer än 0 kr")
            continue

        if amount > money:
            print("Du kan högst satsa: {} kr".format(money))
            continue
        
        return amount
        


for round in range(1,11):
    print("Runda:", round)
    print("Du har {} kr".format(money))
    print("Hur mycket vill du satsa?")
    amount = get_amount()

    gamble(amount)

    print("\n")

print("Spelet är över! Du har nu:", money)

if money > start:
    print("Du vann totalt:", money-start)
else:
    print("Du förlorade totalt:", start-money)

