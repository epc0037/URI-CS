# CSC 110 (Section 1) - Spring 2016
# Week 7: Analysis of Algorithms
# Sorting Algorithms
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

