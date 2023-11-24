import random

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for i in chosen_word:
    display.append("_")

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while(True):
    guess = input("Guess a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            print("Right")
            display[position] = letter
        else:
            print("Wrong")
    print(display)

    if 
