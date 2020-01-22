# Evan Carnevale
# Professor Quitaba Albluwi
# CSC 110 : Survey of Computer Science
# Week 13 : Numerical Analysis
# Homework 13 : Working with Matrices

# Function implemented from class - Tests if the matrix is only 1 row (vector) or not & returns a Bool value
def isVector(matrix):
    if not isinstance(matrix,list):
        return False
    for i in range(len(matrix)):
        if isinstance(matrix[i],list):
            return False
    return True

# Function implemented from class - Tests if the matrix is empty & returns a Bool value
def isEmpty(matrix):
    if matrix == []:
        return True
    return False

# Function implemented from class - Gets number of rows in a given matrix
def getRowSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getRowSize): input not a matrix'
    if isEmpty(matrix):
        return 0
    if isVector(matrix):
        return 1
    return len(matrix)

# Function implemented in class - Gets number of columns in a given matrix
def getColumnSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getColumnSize): input not a matrix'
    if isEmpty(matrix):
        return 0
    if isVector(matrix):
        return len(matrix)
    return len(matrix[0])

# Function implemented in class - returns the size (rows,columns) of a matrix
def getSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getSize): input is not a matrix'
    return int(getRowSize(matrix)), int(getColumnSize(matrix))

# Function implemented from class - Creates a zero vector
def zeroVector(size):
    if size <0:
        return 'Error (zeroVector): invalid size'
    vector = []
    for i in range(size):
        vector = vector + [0]
    return vector

# Function implemented from class - Creates a zero Matrix when given a a certain amount of rows & columns
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

# Function implemented from class - Checks the length of two vectors and returns a Bool value
def isEqualVectorSize(v1,v2):
    if isVector(v1) and isVector(v2) and len(v1) == len(v2):
        return True
    return False

# Function implemented from class - Checks if a given element is a matrix or not - returns a Bool value
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


################-------------------------------------------------------------------------------------------------################
################-------------------------------------------------------------------------------------------------################
################-------------------------------------------------------------------------------------------------################


# Function that returns the sum of two vectors
def vAdd(v1, v2):
    # Check if v1 and v2 are vectors
    if not isVector(v1) or not isVector(v2):
        return 'Error (vAdd): invalid vector input'
    # Checks if the size of v1 and v2 are the same
    if not isEqualVectorSize(v1,v2):
        return 'Error (vAdd): vector size mismatch'
    # Empty list
    result = []
    # Loop that iterates through v1
    for i in range(len(v1)):
        # Addition of vectors
        result = result + [v1[i]+v2[i]]
        # Output
    return result

# Function that checks if all elements in a matrix are 0
def isZeroMatrix(m):
    # m is not a matrix here
    if m == 0:
        # Output
        return False
    # m is an empty list
    if m == []:
        # Output
        return False
    # Check if m is a vector and if the elements are all 0
    if isVector(m) == True and m[0] ==0:
        # Output
        return True
    # Checks if the matrix is actually a matrix
    if isMatrix(m) == True:
        # Loops through matrix
        for i in range(len(m)):
            # Check if the elements in the matrix are NOT 0
            if m[i][i] != 0:
                # Output
                return False
    # Output
    return True

# Function that returns the element at the ith row and jth column
def getElement(matrix,i,j):
    # Invalid cases
    if matrix == 3 or matrix == []:
        # Output
        return 'Error (getElement): Invalid matrix input'
    # Checks the rows and returns an error if the row is negative or larger than the matrix
    if i < 0 or i > len(matrix):
        return 'Error (getElement): illegal row number'
    # Checks the columns and returns an error if the column is negative or larger than the matrix
    if j < 0 or j > len(matrix):
        return 'Error (getElement): illegal column number'
    # If the matrix is a vector, it will just return the element in that row
    if isVector(matrix) == True:
        return matrix[j]
    # Checks if the matrix is not a vector
    if isMatrix(matrix) == True and isVector(matrix) == False:
        # Loops through matrix positions
        for pos in range(len(matrix)):
            # Output
            return matrix[i][j]
        
# Function that creates a zero matrix of the order mxn and adds the start value to the first postion and increments by the step value in the remaining positions           
def numMatrix(m,n,start,step):
    # Cannot have 0 rows or 0 columns
    if m == 0 or n == 0:
        return 'Error (numMatrix): invalid matrix size'
    # Creates a vector
    if m == 1:
        matrix = zeroVector(n)
        # Loops through positions in the column
        for i in range(n):
            # Adds the start value to the ith postion in the vector
            matrix[i] = start
            # Increments the start value by the step value
            start = start + step
            # Output
        return matrix
    # Creates a zero matrix of size mxn
    matrix = zeroMatrix(m,n)
    # Loops through rows and columns
    for i in range(m):
        for j in range(n):
            # Adds the start value to the ith and jth position
            matrix[i][j] = start
            # Increment the start value by the step value
            start = start + step
    # Output
    return matrix

# Function that finds the top left & bottom right corner of the matrix and replaces those elements with x & y
def setCorners(matrix,x,y):
    # Checks if the matrix is empty and returns an error
    if matrix == []:
        return 'Error (setCorners): input is an empty matrix'
    # If the matrix is a string, return an error
    elif matrix == 'lucky':
        return 'Error (setCorners): input is not a matrix'
    # Handles all other remaining cases
    else:
        # Loops through the matrix
        for i in range(len(matrix)):
            # Replaces the first position (top left) with x
            matrix[0][0] = x
            # Replaces the last position (bottom right) with y
            matrix[-1][-1] = y
            # Output
        return matrix
