import random
import json

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'wordlist.json') 
with open(file_path, 'r') as f:
    word_data = json.load(f)

difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
if difficulty in word_data:
    word_list = word_data[difficulty]
else:
    print("Invalid difficulty. Defaulting to easy.")
    word_list = word_data["easy"]


# Logo for Hangman
logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print(logo)

# Stages of Hangman 
stages = [
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]


# choosing random word from list
chosen_word= random.choice(word_list)
# print(chosen_word)

# creating string placeholder which has as many "_" as letters in word
placeholder=""
word_length=len(chosen_word)
for letter in range(word_length):
    placeholder += "_"
print(placeholder)

game_over=False # flag to check if game is over
correct_letters=[] # list to store correct guesses
lives=6

# main game loop
while not game_over:
    print(f"**********************************Lives left: {lives}**********************************")
    display=""
    guess=input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
        continue
#  loop to make display string with correct guesses
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    print(display)
    # counting lives
    if guess not in chosen_word:
        lives -= 1  # Decrement lives only if the guess is incorrect
        print(f"{guess} is not in the word. You lose a life.")
        if lives==0:
            game_over=True
            print(f"****************************It was {chosen_word}.You lose!***********************")
# checking if all letters are guessed
    if "_" not in display:
        game_over=True
        print(f"****************************It is {chosen_word}.You win!***********************")

    print(stages[lives])
