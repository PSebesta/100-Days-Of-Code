# Day 007 Hangman game

This day we are breaking the game into small chucks to work on.

## Step 1 Hangman

This is the code for the first step with 3 todo.

```python
#Step 1 


# to use the random function with have to import it
import random
word_list = ["aardvark", "baboon", "camel"]
# Needed to use the random choice to pick a word from the list and pass it to a variable chsen word
chosen_word = random.choice(word_list)

# The .lower is still a little confusin to me on the proper use of it. I alwys think is need ot add it to the 
# variable 
guess = input("Guess a letter: ").lower()


# This breaks down to for the "letter variable" in Chosen_word it will take it letter from the word and
# check it with the guess of the user if it does not match it will print wrong and if it does match it will 
#print right
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

```


## Step 2 Hangman

In step 2 it ramps up a bit to printing out the blank spaces and filling them in with the correct guess

```python

#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# we created a new varible to collect the display info
display = []
# for the letter variable "in" we have the range function which will go rom 0, len will give us the length of
# the chosen word to finish the range input
for letter in range(len(chosen_word)):

# This will run through the range and add "_" for each position in the range that will be sent to display varriable
    display += "_"
print(display)

# here is the user guess and no matter what they input it will be lowercase with the .lower
guess = input("Guess a letter: ").lower()

# we are passing the range to the postion variable which we will check each number postion
for position in range(len(chosen_word)):
# here we are passing the letter from the chosen word picked from the position we are checking 
    letter = chosen_word[position]
# the letter is no being checked against the user guess 
    if letter == guess:
# if the guess was true we pass the letter to the display list and print the letter instead of the blank space
        display[position] = letter

# here we are printing what is in the display after the guess was checked against the chosen word
print(display)

```

## Step 3 Hangman

This is the code from step 3 not much added on this one just implemented a while loop to run the code till the game is over

```python

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# created a variable for the end of game to stop the while loop
end_game = False

# we added a while loop to keep running the code till the game ends
while not end_game:
# we had to indent all the previos code to be under the while loop
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

# In this code we are checking in display list if blanks are there 
if "_" not in display:
# the variable endgame flips from false above to true that will stop the while loop
    end_game = True
    print("you win.")

```

## Step 4

this code is for step 4 adding lives and art if user guess wrong

```python

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

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

## added this variable so we can hold the amount of lives the user has
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

## added this is staement so if the letter in the guess is not in the chosen word than we drop the lives by 1

    if guess not in chosen_word:
        lives -= 1
## this code is if we reach 0 lives than the en game variable switches to true and the game ends
        if lives == 0:
            end_of_game = True
            print("you lose.")


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

## added the print statement for the art to print based of the index of the lives variable
    print(stages[lives])

```

## step 5

Here is the final code of the game

```python

import random


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"you already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])

```