# Evan Carnevale & Ronin Soto
# Professor Albluwi
# CSC 110
# February 12th, 2016
# Lab 3 - Part 1

# Create three empty lists
List = []
aboveList = []
belowList = []

# input from the user for our loop
n = int(input("Enter the number of sensors: "))

# puts the readings in our empty List
for w in range(n):
    reading = int(input("Enter the amount of the reading for the building: "))
    List += [reading]

# Threshhold from the user
value = int(input("Enter the value of the threshhold: "))

# Loops through our main list to split our readings into ones abpve and below the threshhold
counter2 = 0   
for i in range(n):
    if List[i] > value:
        counter2 += 1
        aboveList = aboveList + [List[i]]
    elif List[i] < value:
        belowList = belowList + [List[i]]
# output for the user
print(counter2)

# sets our maximum/minimum for the items in our List       
MAXIMUM = List[0]
MINIMUM = List[-1]
for k in range(len(List)):
    if List[k] > MAXIMUM:
        MAXIMUM = List[k]
for j in range(len(List)):
    if List[j]< MINIMUM:
        MINIMUM = List[j]
        
    
    

# output for the user
print(aboveList)
print(belowList)
print(MAXIMUM)
print(MINIMUM)
