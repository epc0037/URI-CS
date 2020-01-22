# CSC 110 - Spring 2016 - Section 1
# Week 4 (Functions) - Class Activities (Tuesday)
# Exercise 2

def flip(inputList):
   last = len(inputList)-1
   temp = inputList[0]
   inputList[0] = inputList[last]
   inputList[last] = temp
   return inputList

def flop(inputList):
   for i in range(len(inputList)):
       inputList[i] = inputList[i] + 1
   return inputList

def flip_flop(inputList1, inputList2):
    last1 = len(inputList1) - 1
    last2 = len(inputList2) - 1

    x1 = inputList1[0]
    x2 = inputList2[0]
    y1 = inputList1[last1]
    y2 = inputList2[last2]

    inputList1[0] = y2
    inputList1[last1] = x2
    inputList2[0] = y1
    inputList2[last2] = x1

    return inputList1, inputList2

# --------- Start of main program -----------

a = [1, 2, 3, 4, 5, 6, 7]
b = [10, 20, 30, 40, 50]

x = flip(a)
print(x)
y = flop(b)
print(y)
z1, z2 = flip_flop(x,y)
print(z1, z2)
# ------------ End of main program -------------
