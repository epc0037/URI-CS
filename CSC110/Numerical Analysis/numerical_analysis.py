# Evan Carnevale
# CSC 110 : Survey of Computer Science
# Professor Albluwi
# Week 13 : Numerical Analysis
# Class Activitis (Tuesday)

def isVector(m):
    isList = False
    if isinstance(m,list) == True:
        for i in range(len(m)):
            if isinstance(m[i],list) == True:
                return False
        isList = True
    return isList

def isMatrix(m):
    counter = 0
    counter1 = 0
    if isinstance(m, list) != True:
        return False
    else:
        for i in range(len(m)):
            if isVector(m[i]):
                counter = counter + len(m[i])
                counter1 = len(m[i])
        if counter == len(m) * counter1:
            return True
        else:
            return False

def zeroVector(size):
    vector = []
    if size < 0:
        return 'Error (zeroVector): invalid size'
    else:
        for i in range(size):
            vector = vector + [0]
    return vector

def zeroMatrix(rows, columns):
    vector = []
    for i in range(rows):
        vector = vector + []
        for i in range(columns):
            vector = vector[i] + [0]
    return vector

def getColumnSize(matrix):
    return

def getRow(matrix):
    return
