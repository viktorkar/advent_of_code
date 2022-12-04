# Desired Outcomes
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

# Available Moves
ROCK = 'A'
PAPER = 'B'
SCISSOR = 'C'

# Points
WIN_P = 6
DRAW_P = 3
LOSE_P = 0

####################################################################################
def convert_move(my_move): # For task 1
    if my_move == 'Y':   
        return PAPER
    elif my_move == 'X':
        return ROCK
    elif my_move == 'Z':
        return SCISSOR

####################################################################################
def get_move_score(my_move):
    if my_move == ROCK:     # Rock -> 1 point
        return 1
    elif my_move == PAPER:  # Paper -> 2 points
        return 2
    elif my_move == SCISSOR: # Scissor -> 3 points
        return 3

####################################################################################
def calc_round_score(opponents_move, my_move):
    total_score = get_move_score(my_move)

    if opponents_move == ROCK:
        if my_move == PAPER:        # Paper -> Win
            total_score += WIN_P
        elif my_move == ROCK:       # Rock -> Draw
            total_score += DRAW_P
        elif my_move == SCISSOR:    # Scissor -> Loss
            total_score += LOSE_P

    elif opponents_move == PAPER:  
        if my_move == PAPER:        # Paper -> Draw
            total_score += DRAW_P
        elif my_move == ROCK:       # Rock -> Loss
            total_score += LOSE_P
        elif my_move == SCISSOR:    # Scissor -> Win
            total_score += WIN_P

    elif opponents_move == SCISSOR:  
        if my_move == PAPER:        # Paper -> Loss
            total_score += LOSE_P
        elif my_move == ROCK:       # Rock -> Win
            total_score += WIN_P
        elif my_move == SCISSOR:    # Scissor -> Draw
            total_score += DRAW_P

    return total_score

####################################################################################
def choose_move(opponent, input):
    if opponent == ROCK:
        if input == WIN:        # Paper -> Win
            return PAPER
        elif input == DRAW:     # Rock -> Draw
            return ROCK
        elif input == LOSE:     # Scissor -> Loss
            return SCISSOR

    elif opponent == PAPER: 
        if input == WIN:        # Scissor -> Win
            return SCISSOR
        elif input == DRAW:     # Paper -> Draw
            return PAPER
        elif input == LOSE:     # Rock -> Lose
            return ROCK

    elif opponent == SCISSOR:  
        if input == WIN:        # Rock -> Win
            return ROCK
        elif input == DRAW:     # Scissor -> Draw
            return SCISSOR
        elif input == LOSE:     # Paper -> Lose
            return PAPER
    

####################################################################################
def solve_task1(filename):
    totalScore = 0

    with open(filename) as f:
        for line in f:
            opponent_move, my_move = line.split(" ")
            opponent_move = opponent_move.strip()
            my_move = my_move.strip()

            my_move = convert_move(my_move) # converts input to ROCK,PAPER,SCISSOR
            totalScore += calc_round_score(opponent_move, my_move)

    print("Task1: Total score:", totalScore)

####################################################################################
def solve_task2(filename):
    totalScore = 0

    with open(filename) as f:
        for line in f:
            opponents_move, my_move = line.split(" ")
            opponents_move = opponents_move.strip()
            my_move = my_move.strip()

            my_move = choose_move(opponents_move, my_move)
            totalScore += calc_round_score(opponents_move, my_move)

    print("Task2: Total score:", totalScore)

solve_task1("input.txt")
solve_task2("input.txt")