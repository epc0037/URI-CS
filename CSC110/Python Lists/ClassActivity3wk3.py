# Evan Carnevale
# Professor Albluwi
# CSC 110
# February 11th, 2016
# Class Activity 3: Week 3
# This program will create two loops for the user based upon the information
# they wish to enter.

counter1 = 0
List = []
n = int(input("Enter the number of sensors: "))

while counter1 < n:
    value = int(input("Enter the value of the threshhold: "))
    List += [value]
    counter1 += 1
print(List)
    
counter2 = 0   
for i in range(n):
    if value > THRESHHOLD:
        counter2 += 1

print(counter2)
