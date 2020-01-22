# CSC 110 - Spring 2016
# Week 7: Analysis of Algorithms
# Evan Carnevale & Devin Gould

#--------------------------------------------------
def phoneLinearSearch(names, phones, name):
    for i in range(len(names)):
        if name == names[i]:
            return phones[i]

    return -1

def linearSearch(inputList, value):
    for i in range(len(inputList)):
        if value == inputList[i]:
            return i
    return -1
        

# Function to read the names and phones into lists from a given file
# the input file is formatted in like the following: 'Alice,434-5549'
def getLists():
    fname = input("Enter name of data file: ")
    inFile = open(fname,'r')
    reading = inFile.readline()
    names = []
    phones = []
    while reading != '':
        name, phone = reading.strip().split(',')
        names = names + [name]
        phones = phones + [phone]
        reading = inFile.readline()
    inFile.close()
    return names, phones
#--------------------------------------------------

# function to find the name and return associated phone number
# using binary search
# if name is not found - return phone number = ""
def binarySearch(nameList, phoneList, name):
    start = 0
    end = len(nameList)

    startMarker = start
    endMarker = end

    while (endMarker - startMarker) != 1:
        middleMarker = (endMarker + startMarker) // 2
        if name < nameList[middleMarker]:
            endMarker = middleMarker
        elif name > nameList[middleMarker]:
            startMarker = middleMarker
        elif name == nameList[middleMarker]:
            return phoneList[middleMarker]

    middleMarker = (endMarker + startMarker) // 2
    if name == nameList[middleMarker]:
            return phoneList[middleMarker]
    return ''

#---------------------------------------------------

# function to read n names from a given filename
# Note: use the file: randomNames.txt
def getNames(fileName, n):
    inFile = open(fileName, 'r')
    names = []
    for i in range(n):
        reading = inFile.readline().strip()
        if reading == '':
            return 'n exceeds file contents'
        names = names + [reading]
    return names
#---------------------------------------------------

# function to generate a random phone number in the format
# (###) ###-####
def randomPhone():
    # ... Put your code here
     return ''
#---------------------------------------------------

# function to generate n random phone numbers
# (###) ###-####
def generaterandomPhones(n):
    # ... Put your code here
     return ''
#---------------------------------------------------

# function to analyze the efficency of binary search
def binarySearchAnalysis():
    # ... Put your code here
     return ''
#---------------------------------------------------
def selectionSort(inputList):
    for marker in range(len(inputList)-1):
        # Find minimum in unsorted List
        minPosition = marker
        for i in range(marker+1, len(inputList)):
            if(inputList[i] < inputList[minPosition]):
                minPosition = i
        # Swap the minimum value with
        # the first number in the unsorted list (at the marker)
        if (minPosition != marker):
            temp = inputList[minPosition]
            inputList[minPosition] = inputList[marker]
            inputList[marker] = temp
    return inputList
#---------------------------------------------------
# Main Function
def main():
    # Get the lists
    names, phones = getLists()
    # Get the name to search for
    theName = input("Enter the name to search for: ")

    # Find the phone number for the given name
    phoneNum = binarySearch(names, phones, theName)
    if phoneNum == "":
        print("Name not found")
    else:
        print("The phone number for ", theName, " is ", phoneNum)
