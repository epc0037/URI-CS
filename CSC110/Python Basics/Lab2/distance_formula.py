# Evan Carnevale
# Professor Albluwi
# CSC 110 - Section 1
# Lab 2
# Part 3 (Challenge)
# This program will prompt the user to give us two points
# the program will use the distance formula to compute
# the distance between the points.

# input for the user - 4 coordinate points
x1 = float(input("Enter a value for x1"))
x2 = float(input("Enter a value for x2"))
y1 = float(input("Enter a value for y1"))
y2 = float(input("Enter a value for y2"))

# distance formula
_distance = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

print(_distance)
