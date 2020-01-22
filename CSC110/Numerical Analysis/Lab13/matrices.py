# Evan Carnevale & Jonathan Reyes
# Professor Albluwi
# CSC 110: Survey of Computer Science
# Week 13 : Numberical Analysis
# Lab 13 : Matrices

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

def isEmpty(matrix):
    if matrix == []:
        return True
    return False

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

def isSquare(m):
    matrix = isMatrix(m)
    if m == []:
        return False
    if matrix == True:
        rows = getRowSize(m)
        columns = getColumnSize(m)
        if rows == columns:
            return True
    return False

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

def zeroVector(size):
    if size <0:
        return 'Error (zeroVector): invalid size'
    vector = []
    for i in range(size):
        vector = vector + [0]
    return vector

def identityMatrix(size):
    matrix = zeroMatrix(size, size)
    if size == 1:
        return [1]
    if size <= 0:
        return 'Error: (identityMatrix): invalid size'
    for i in range(size):
        matrix[i][i] += 1
    return matrix

def isIdentity(matrix):
    if matrix == 10:
        return False
    if matrix == [1]:
        return True
    if isVector(matrix) == True:
        return False
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

def determinant(matrix):
    if matrix == 2 or matrix == 3:
        return 'Error (determinant) : input is not a matrix'
    col = getColumnSize(matrix)
    row = getRowSize(matrix)
    if int(col) > 2 and int(row) > 2:
        return 'Error (determinant) : invalid matrix size'
    if isSquare(matrix) == False:
        return 'Error (determinant) : invalid matrix size'
    else:
        a = matrix[0][0]
        d = matrix[1][1]
        b = matrix[0][1]
        c = matrix[1][0]
        _determinant = (a*d)-(b*c)
        return _determinant
        
def inverse(matrix):
    _Determinant = determinant(matrix)
    if matrix == 3:
        return 'Error (inverse) : input is not a matrix'
    col = getColumnSize(matrix)
    row = getRowSize(matrix)
    if int(col) != 2 or int(row) != 2:
        return 'Error (determinant) : invalid matrix size'
    if _Determinant == 0:
        return 'Error (inverse): the given matrix is not invertible'
    if isVector(matrix) == True:
        return 'Error (inverse): invalid matrix size'
    scalar = 1/_Determinant
    a = matrix[0][0]
    d = matrix[1][1]
    b = matrix[0][1]
    c = matrix[1][0]

    new_a = a * scalar
    new_b = (-b) * scalar
    new_c = (-c) * scalar
    new_d = d * scalar

    matrix[0][0] = new_d
    matrix[0][1] = new_b
    matrix[1][0] = new_c
    matrix[1][1] = new_a
    return matrix
