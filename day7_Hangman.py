import random
#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

correct = 0
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#Create blanks
display = []
word_length = len(chosen_word)
for i in range(word_length):
    display.append("_")

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
while not end_of_game:
    correct = 0
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print("Right")
    else:
        print("Wrong")

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
            correct += 1
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!!")