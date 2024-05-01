############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
all_cards = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 , 'A':[1, 11]}
print("Welcome to the Blackjack game")
another_game = 'Y'
def calculate_score(cards):
    have_A = 0
    score = 0
    for card in cards:
        if card == 'A':
            have_A += 1
        else:
            score += all_cards[card]
    while have_A > 0:
        if score + 11 > 21:
            score += 1
        have_A -= 1
    if score > 21:
        return 0
    else:
        return score
        
while another_game == "Y":
    your_card = [random.choice(list(all_cards.keys())), random.choice(list(all_cards.keys()))]
    print(f"Your cards: {your_card}")
    bot_card = [random.choice(list(all_cards.keys()))]
    print(f"Bot's first card: {bot_card}")
    your_score = calculate_score(your_card)
    if your_score == 21:
        print("You win with Black jack!!!")
        continue
    another_card = input("Type 'Y' to get another card, 'N' to pass: ")
    if another_card == 'Y':
        your_card.append(random.choice(list(all_cards.keys())))
    bot_card.append(random.choice(list(all_cards.keys())))
    bot_score = calculate_score(bot_card)
    if bot_score == 21:
        print("You lose with bot's Black jack!!!")
    elif bot_score < 17:
        bot_card.append(random.choice(list(all_cards.keys())))
    print(f"Your final hand: {your_card}")
    your_score = calculate_score(your_card)
    print(f"Bot's final hand: {bot_card}")
    bot_score = calculate_score(bot_card)
    if your_score > bot_score:
        print("You win!!")
    elif your_score < bot_score:
        print("You lose!!")
    else:
        print("Draw")
    another_game = input("Another game? (Y/N): ")
