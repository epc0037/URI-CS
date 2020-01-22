# CSC 110 (Section 1) - Spring 2016
# Week 7: Analysis of Algorithms
# Sorting Algorithms
# Homework 7 - Problem 2
# Evan Carnevale - 100460662

# --------------- Simple Sort ------------------
def simpleSort(inputList):
    MAX = 1000000
    sortedList=[]
    for i in range(len(inputList)):
        minPosition = 0
        for j in range(1, len(inputList)):
            if(inputList[j] < inputList[minPosition]):
                minPosition = j
        sortedList = sortedList + [inputList[minPosition]]
        inputList[minPosition] = MAX
    return sortedList

# ------------ Insertion Sort -----------------
def insertionSort(inputList):
    for marker in range(1, len(inputList)):
        currentValue = inputList[marker]
        previousIndex = marker - 1
        #slide back the list until you find the smallest
        while previousIndex >=0:
            if currentValue < inputList[previousIndex]:
                # swap
                temp = inputList[previousIndex]
                inputList[previousIndex] = inputList[previousIndex + 1]
                inputList[previousIndex + 1] = temp
                previousIndex = previousIndex - 1
            else:
                break
    return inputList
# ---------------- Selection Sort --------------
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

# --------------- Simple Sort 2 ------------------

def simpleSort2(inputList):
    MAX = 1000000
    sortedList=[]
    for i in range(len(inputList)):
        minPosition = 0
        for j in range(1, len(inputList)):
            if(str(inputList[j])) < str(inputList[minPosition]):
                minPosition = j
        sortedList = sortedList + [inputList[minPosition]]
        inputList[minPosition] = MAX
    return sortedList


# --------------- Read Data ------------------

def readData(filename):
    inFile = open(filename,'r')
    years = []
    cities = []
    countries = []
    line = inFile.readline()
    while line != '':
        year, place = line.split('\t')
        city, country = place.split(',')
        country = country.strip()
        years = years + [int(year)]
        cities = cities + [city]
        countries = countries + [country]
        line = inFile.readline()
    inFile.close()
    return years, cities, countries

# --------------- Sort Lists ------------------

def sortLists(cities, countries):
    sort_city = simpleSort2(cities)
    sort_country = simpleSort2(countries)

    return sort_city, sort_country

# --------------- Dual Sort ------------------

def dualSort(list1, list2):

    MAX = 1000000
    sortedList=[]
    for i in range(len(list1)):
        minPosition = 0
        for j in range(1, len(list1)):
            if(list1[j] < list1[minPosition]):
                minPosition = j
        sortedList = sortedList + [list1[minPosition]]
        list1[minPosition] = MAX




    
    for marker in range(1, len(list2)):
        currentValue = list2[marker]
        previousIndex = marker - 1
        #slide back the list until you find the smallest
        while previousIndex >=0:
            if currentValue < list2[previousIndex]:
                # swap
                temp = list2[previousIndex]
                list2[previousIndex] = list2[previousIndex + 1]
                list2[previousIndex + 1] = temp
                previousIndex = previousIndex - 1
            else:
                break
    return sortedList, list2
    
