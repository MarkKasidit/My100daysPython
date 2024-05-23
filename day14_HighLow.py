from utils import highlow_arts as hla, highlow_data as hld
import random as rd
print(hla.logo)
score = 0
while True:
    A = rd.choice(hld.data)
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(hla.vs)
    while True:
      B = rd.choice(hld.data)
      if A != B:
          break
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
    ans = input("Who has more followers? Type 'A' or 'B': ")
    if ans == 'A':
        if A['follower_count'] > B['follower_count']: 
            score += 1
            print(f"You right! current score: {score}\n")
            continue
        else:
            print(f"Sorry, that's wrong. Final score = {score}")
            break

    elif ans == 'B':
        if B['follower_count'] > A['follower_count']: 
            score += 1
            print(f"You right! current score: {score}\n")
            continue
        else:
            print(f"Sorry, that's wrong. Final score = {score}")
            break
    else:
        print("You break the rule!")
        break