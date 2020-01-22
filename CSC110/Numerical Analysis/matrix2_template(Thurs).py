# CSC110: Spring 2016 (Section 1)
# Week 13: Numerical Analysis
# Class Activities (Thursday)

# -------------------------------
# The following functions were developed last class

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

# ---------------------------------
# The following functions are provided for you - for convenience

def isEmpty(matrix):
    if matrix == []:
        return True
    return False

def printMatrix(matrix):
    if isVector(matrix):
        print(matrix)
    elif isMatrix(matrix):
        for i in range(len(matrix)):
            print(matrix[i])
    else:
        print('Error (printMatrix): not a matrix')

def zeroVector(size):
    if size <0:
        return 'Error (zeroVector): invalid size'
    vector = []
    for i in range(size):
        vector = vector + [0]
    return vector

def isEqualVectorSize(v1,v2):
    if isVector(v1) and isVector(v2) and len(v1) == len(v2):
        return True
    return False

def vScalarMult(vector, num):
    if not isVector(vector):
        return 'Error (vScalarMult): invalid vector input'
    for i in range(len(vector)):
        vector[i] = vector[i]*num
    return vector

def vAdd(v1, v2):
    if not isVector(v1) or not isVector(v2):
        return 'Error (vAdd): non-vector input'
    if not isEqualVectorSize(v1,v2):
        return 'Error (vAdd): vector size mismatch'
    result = []
    for i in range(len(v1)):
        result = result + [v1[i]+v2[i]]
    return result

def vSubtract(v1,v2):
    return vAdd(v1,vScalarMult(v2,-1))

# transpose a vector
def vTranspose(vector):
    if not isVector(vector):
        return 'Error (vTranspose): input is not a vector'
    # if the vector is empty or has only one element, the transpose is the same
    if vector == [] or len(vector) == 1:
        return vector
    t = []
    for i in range(len(vector)):
        t = t + [[vector[i]]]
    return t
    
# transpose
def transpose(matrix):
    if not isMatrix(matrix):
        return 'Error (transpose): input is not a matrix'
    if isEmpty(matrix):
        return []
    if isVector(matrix):
        return vTranspose(matrix)
    r,c = getSize(matrix)
    t = zeroMatrix(c,r)
    for i in range(c):
        for j in range(r):
            t[i][j] = matrix[j][i]
    return t

# ---------------------------------
# put your solutions here

# Problem 1:
def add(m1, m2):
    print('Add your implementation here')

# Problem 2:
def scalarMult(matrix, num):
    print('Add your implementaion here')

# Problem 3: 
def subtract(m1,m2):
    print('Add your implementaion here')

# Problem 4:
def isSymmetric(matrix):
    print('Add your implementaion here')

# Problem 5:
def isEqualSize(m1,m2):
    print('Add your implementaion here')
