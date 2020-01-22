# Evan Carnevale
# Professor Albluwi
# CSC 110 - Section 1
# Lab 2
# Part 2
# This program will determine how many of a set of 10 numbers are even
# and how many are odd. Each number will be read one at a time and a final
# statement will print the results for the user.

# number of integers we know we need to use
number_of_ints = 10

# accumulators
i = 0
even = 0
odd = 0

# loop through 10 times
while i < number_of_ints:
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
        
    # increment the counter
    i += 1

# print the output
print("Out of the 10 numbers: ", even, " are even numbers.")
print("Out of the 10 numbers: ", odd, " are odd numbers.")
