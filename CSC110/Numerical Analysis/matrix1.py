# Evan Carnevale
# CSC110: Spring 2016 (Section 1)
# Week 13: Numerical Analysis
# Class Activities (Thursday)

def isEmpty(matrix):
    if matrix == []:
        return True
    return False

# [] is a vector
# [1,2,3] is a vector
# 3 is not a vector
# [[1,2]] is not a vector
# [[1,2],[2,3]] is not a vector
def isVector(matrix):
    if not isinstance(matrix,list):
        return False
    for i in range(len(matrix)):
        if isinstance(matrix[i],list):
            return False
    return True

def isMatrix(matrix):
    # if a single item --> Not Matrix
    if not isinstance(matrix,list):
        return False
    # if vector --> Matrix
    if isVector(matrix):
        return True
    # if different lengths --> not Matrix
    if isinstance(matrix[0],list):
        rowLength = len(matrix[0])
    else:
        return False
    for i in range(len(matrix)):
        if ((not isinstance(matrix[i],list)) or (len(matrix[i])!= rowLength)):
            return False
    return True

# Vector Operations
def zeroVector(size):
    if size <0:
        return 'Error (zeroVector): invalid size'
    vector = []
    for i in range(size):
        vector = vector + [0]
    return vector

# zeroMatrix
def zeroMatrix(rows, columns):
    if rows < 0 or columns < 0:
        return 'Error (zeroMatrix): invalid size'
    if rows == 1:
        return zeroVector(columns)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row = row + [0]
        matrix = matrix + [row]
    return matrix

# get number of rows
def getRowSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getRowSize): input not a matrix'
    if isEmpty(matrix):
        return 0
    if isVector(matrix):
        return 1
    return len(matrix)

# get number of columns
def getColumnSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getColumnSize): input not a matrix'
    if isEmpty(matrix):
        return 0
    if isVector(matrix):
        return len(matrix)
    return len(matrix[0])

def getSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getSize): input is not a matrix'
    return getRowSize(matrix), getColumnSize(matrix)

def printMatrix(matrix):
    if isVector(matrix):
        print(matrix)
    elif isMatrix(matrix):
        for i in range(len(matrix)):
            print(matrix[i])
    else:
        print('Error (printMatrix): not a matrix')

def add(m1,m2):
    result = []
    # Check if m1 and m2 are vectors
    if isVector(m1) == True and isVector(m2) == True:
        for i in range(len(m1)):
            result += [m1[i] + m2[i]]
        return result
    # Check for errors
    check1 = getSize(m1)
    check2 = getSize(m2)
    if check1 != check2:
        return "Error (add): matrix size mismatch"
    if not isMatrix(m1):
        return "Error (add): invalid matrix input"
    elif not isMatrix(m2):
        return "Error (add): invalid matrix input"
    # Loop through ad add matrices
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

def scalarMult(m1,num):
    result = []
    # Check For Errors
    if not isMatrix(m1):
        return "Error (GetElement): invalid matrix input"
    if isEmpty(m1) == True:
        return "Error (GetElement): matrix is empty"
    if isVector(m1) == True:
        for i in range(len(m1)):
            result += [m1[i] * num]
        return result
    # Loop through and multiply each element by num
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] * num)
        result.append(row)
    return result

def subtract(m1,m2):
    return add(m1, scalarMult(m2, -1))

def isSymmetric(m):
    return

def isEqualSize(m1,m2):
    if not isMatrix(m1) or not isMatrix(m2):
        return False
    check1 = getSize(m1)
    check2 = getSize(m2)
    if check1 != check2:
        return False
    else:
        return True
