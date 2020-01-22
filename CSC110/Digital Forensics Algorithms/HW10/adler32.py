# Evan Carnevale
# Professor Albluwi
# CSC 110 - Survey of Computer Science
# Homework 10 - Digital Forensics
# This program implements the checksum algorithm Adler-32 (32-bits).


# Function that calculates A, which is initialized at 1, summed by the decimal
# values of the characters in a string (built in Python ord() function) and then modulized by 65521.
def computeA(inputString):
    sumA = 1
    for i in range(len(inputString)):
        sumA = sumA + ord(inputString[i])
        A = sumA % 65521
    return A

# Function that calculates B, which is accumulated by the values of A and modulized by 65521.
def computeB(inputString):
    sumB = 1
    B = 0
    for i in range(len(inputString)):
        sumB = sumB + ord(inputString[i])
        B = B + sumB % 65521
    return B

# Function that calculates the Adler-32 hash by calculating B, multiplying B by 65536 and adding A to that value.
def adler32(inputString):
    A = 1
    B = 0
    ADLER = 65536
    for i in range(len(inputString)):
        A = A + ord(inputString[i])
        B = B + A % 65521
        _adler32 = (B * ADLER) + A
    return _adler32
