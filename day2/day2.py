LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'


def get_move_score(you):
    if you == 'Y':      # Paper -> 1 point
        return 2
    elif you == 'X':    # Rock -> 2 points
        return 1
    elif you == 'Z':    # Scissor -> 3 points
        return 3

def calc_round_score(opponent, you):
    move_score = get_move_score(you)

    if opponent == 'A': # Rock
        if you == 'Y':      # Paper -> Win
            return 6 + move_score
        elif you == 'X':    # Rock -> Draw
            return 3 + move_score
        elif you == 'Z':    # Scissor -> Loss
            return 0 + move_score

    elif opponent == 'B': # Paper    
        if you == 'Y':      # Paper -> Draw
            return 3 + move_score
        elif you == 'X':    # Rock -> Loss
            return 0 + move_score
        elif you == 'Z':    # Scissor -> Win
            return 6 + move_score

    else: # Scissors    
        if you == 'Y':      # Paper -> Loss
            return 0 + move_score
        elif you == 'X':    # Rock -> Win
            return 6 + move_score
        elif you == 'Z':    # Scissor -> Draw
            return 3 + move_score

def choose_move(opponent, input):
    print(opponent, )
    if opponent == 'A': # Rock
        if input == WIN:      # Paper -> Win
            return 'Y'
        elif input == DRAW:    # Rock -> Draw
            return 'X'
        elif input == LOSE:    # Scissor -> Loss
            return 'Z'

    elif opponent == 'B': # Paper    
        if input == WIN:      # Scissor -> Win
            return 'Z'
        elif input == DRAW:    # Paper -> Draw
            return 'Y'
        elif input == LOSE:    # Rock -> Lose
            return 'X'

    else: # Scissors    
        if input == WIN:      # Rock -> Win
            return 'X'
        elif input == DRAW:    # Scissor -> Draw
            return 'Z'
        elif input == LOSE:    # Paper -> Lose
            return 'Y'
    


def play(filename):
    totalScore = 0
    with open(filename) as f:
        for line in f:
            opponent, you = line.split(" ")
            opponent = opponent.strip()
            you = you.strip()
            you = choose_move(opponent.strip(), you.strip())
            print(you)
            totalScore += calc_round_score(opponent, you)

    print("Total score:", totalScore)

play("input.txt")