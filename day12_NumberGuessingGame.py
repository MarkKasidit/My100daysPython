import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
gen_number = random.randint(0, 100)
have_mode = {"easy":10, "hard":5}
def gameplay(mode):
    round = have_mode[mode]
    while True:
        print(f"You have {round} attempts remaining to guess.")
        guess = int(input("Make a guess:"))
        if guess > gen_number:
            print("Too high.") 
            round -= 1
        elif guess < gen_number:
            print("Too low.") 
            round -= 1
        else:
            print(f"You win! The answer is {guess}.")
            break
        if round == 0:
            print("Game Over!")
            break
        print("Guess again.")
        
gameplay(mode)