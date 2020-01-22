# Evan Carnevale
# Professor Albluwi
# CSC 110 - Section 1
# Lab 2
# Part 4 (Challenge)
# This program will create a guess the number game!!
# A random number between 1 and 10 will be generated from the random module
# and the user will be prompted to guess the number. If the guess is too high,
# or too low, the user will be told such. Output will include the number of guesses

# we need the random module
import random

# generate the random number between 1 and 10
number = random.randint(1,10)

# initialize the counter
_guesses = 0
_try = 0

# evaluate if the guess was correct or not
while _try != number:
    _try = int(input("Guess a random number between 1 and 10"))
    if _try < number:
        print("Your guess was too low!")
        _guesses +=1
    elif _try > number:
        print("Your guess was too high!")
        _guesses += 1

print("You guessed the correct number!!!")
    
