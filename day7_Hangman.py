import random
from utils import hangman_arts as ha, hangman_words as hw

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hw.word_list)

print(ha.logo)
display = []
lives = 6
word_length = len(chosen_word)
for i in range(word_length):
    display.append("_")

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
          
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose...")
    print(ha.stages[lives])
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!!")