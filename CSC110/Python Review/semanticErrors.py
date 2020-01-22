# This function increments the fourth element in a list
# if the list has no fourth element it returns an error
def incrementFourth(inputList):
    if len(inputList)<4:
        return 'Error: No fourth element'
    return inputList[3] + 1

# This function swaps two elements in a list as determined by the given indices
def swap(inputList, index1, index2):
    length = len(inputList)
    if ((index1>= length) or (index2>= length)):
        return 'Error index is larger than list length'
    temp = inputList[index1]
    inputList[index1] = inputList[index2]
    inputList[index2] = temp
    return inputList
    
# This function doubles the value of the first element and return the updated list
# if the list is empty it returns an empty
def doubleFirst(inputList):
    if inputList == []:
        return []
    else:
        inputList[0] = inputList[0]*2
        return inputList

# This function shifts the elements of a list to the left by one
# Example: [1,2,3,4] -->> [2,3,4,1]
# Example: [a,b,c,d,e] -->> [b,c,d,e,a]
def shiftLeft(inputList):
    length = len(inputList)
    newList = [inputList[length-1]]
    for i in range(length -1):
        newList = newList + [inputList[-1]]
    return newList
        

# This function mutliplies the elements of two lists one by one
# the length of the two lists should be equal
# Example: [1,2,3,4]*[10,20,30,40] -->> [10,40,90,160]
# Example: [0,0,1,1]*[3,4,5,6] -->>[0,0,5,6]
def multList(list1, list2):
    if len(list1) != len(list2):
        return 'Error'
    result = []
    for i in range(len(list1)):
        r = list1[i]*list2[i]
        result = result + [r]
    return result

