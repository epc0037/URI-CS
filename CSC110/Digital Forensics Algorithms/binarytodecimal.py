# Evan Carnevale
# CSC 110 - Digital Forensics
# Class Activity
# This program will convert a string representing a binary number to a decimal number.

def binaryToDecimal(binary):
    decimal = 0
    power = len(binary) - 1
    for i in range(len(binary)):
        decimal = decimal + int(binary[i])*(2**power)
        power = power - 1
    return decimal

def decimalToBinary(decimal):
    binary = ''
    power = 7
    for i in range(8):
        if decimal >= (2**power):
            binary = binary + '1'
            decimal = decimal - (2**power)
        else:
            binary = binary + '0'
        power = power -1
    return binary

def checksum8(inputString):
    asciiSum = 0
    # convert to ASCII
    for i in range(len(inputString)):
        asciiSum = asciiSum + ord(inputString[i])
    checksum = asciiSum % 256
    return checksum
        
