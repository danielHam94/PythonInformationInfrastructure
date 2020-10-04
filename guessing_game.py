# Daniel Ham
# Guessing Game

# **********************INSTRUCTIONS**********************
# Use the random
# module to write thisguessing game.The number the computer chooses
# should change each time you run the program.
# 
# Keep track of the number of tries it takes the user to guess it.
# ********************************************************

import random

# Game title
print("\t Welcome to 'Guess My Number'!")

print("\nI'm thinking of a number between 1 and 100. \n" \
      "Try to guess it in as few attempts as possible.\n")

# Get a random number between 1 and 100
random_number = random.randrange(1,101)

# Variable to hold count of tries
tries = 0

# While loop to get guess
while True:
    guess = int(input("Take a guess: "))
    tries += 1

    # If-else statement to tell user higher, lower, or correct
    if guess < random_number:
        print("Higher...")
    elif guess > random_number:
        print("Lower...")
    else:
        print("You guessed it! The number was", random_number \
              ,"\nAnd it only took you", tries, "tries!")
        break
