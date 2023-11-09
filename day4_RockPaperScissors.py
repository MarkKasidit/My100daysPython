import random
n = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choice = ["Rock", "Paper", "Scissors"]
if n >= 3 or n < 0: print("Error Input: You loseee")
else:
    print(f"I choose: {choice[n]}")
    m = random.randint(0, 2)
    print(f"Computer choose: {choice[m]}")
    if n == m: print("It's a draw.")
    elif n == 0 and m == 2: print("You win!!!")
    elif n == 1 and m == 0: print("You win!!!")
    elif n == 2 and m == 1: print("You win!!!")
    else: print("You lose TT")