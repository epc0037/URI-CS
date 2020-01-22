# Evan Carnevale
# Professor Albluwi
# CSC 110 - Section 1
# Lab 2
# Part 1
# This program will implement exponentials without using the ** operator

# global variables used as counters/sum
_sum = 1
count = 0

# input from the user
a = int(input("Enter an integer that represents the base"))
b = int(input("Enter an integer that represents the exponent"))

# loop
while count < b:
    _sum = _sum * a
    count = count + 1

# output for the user
print(_sum)
