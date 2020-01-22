# Evan Carnevale
# CSC 110 - Survey of Computer Science
# Professor Albluwi
# Homework 3 - Problem 1
# This program will generate a list containing
# all the odd numbers between 100 and 500 except 227 and 355.

# create an empty number list & set the values we wish to remove from the list
numList = []
a = 227
b = 355

# for loop that goes from 100 to 500 (501 because it doesn't include the last value)
# if i in the range 100 to 500 has a remainder when divided by 2, i is added to the list
# the last statements are nested if statements which remove the values 227 and 355 from our list
for i in range(100,501):
    if i % 2 != 0:
        numList = numList + [i]
        if a in numList:
            numList.remove(a)
        if b in numList:
            numList.remove(b)
            
# final output that prints the list to the user, except 227 and 355        
print(numList)
    
