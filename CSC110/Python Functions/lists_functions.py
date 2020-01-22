# CSC 110 - Spring 2016 - Section 1
# Week 4 (Functions) - Class Activities (Tuesday)
# Exercise 3

#listMax Function
# Take a list of numbers and return the maximum value
def listMax(inputList):
    max = inputList[0]
    for i in range(len(inputList)):
        if inputList[i] > max:
            max = inputList[i]
    return max

#listMin Function
# take a list of numbers and return the minimum value
def listMin(inputList):
    min = inputList[0]
    for i in range(len(inputList)):
        if inputList[i] < min:
            min = inputList[i]
    return min

# isPositive Function
# take a list of numbers as input and return true if all values are positive and false otherwise
def isPositive(myList):
    for j in range(len(myList)):
        if myList[j] <=0:
            return False
    return True

# listRange
# compute the rang of a list of numbers
# range = max - min
def listRange(iList):
    return (max(iList) - min(iList))

# compute the sum of a list of numbers
def listSum(rawList):
    sum = 0
    for k in range(len(rawList)):
        sum = sum + rawList[k]
    return sum

# compute the average of a list of numbers
def listAverage(dataList):
    return (listSum(dataList)/len(dataList))
