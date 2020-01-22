def checkSum16(inputString):
    checkSum = 0
    i = 0
    if len(inputString) % 2 == 1:
        inputString = inputString + " "
    while i < len(inputString):
        firstLetter = inputString[i]
        secondLetter = inputString[i+1]
        a1 = ord(firstLetter)
        a2 = ord(secondLetter)
        b1 = decimalToBinary(a1)
        b2 = decimalToBinary(a2)
        binary = b1 + b2
        decimal = binaryToDecimal(binary)
        checkSum = checkSum + decimal
        i = i + 2
            
    checkSum = checkSum % (2**16)
    return checkSum
            
            
def binaryToDecimal(binary):
    decimal = 0
    power = len(binary) - 1
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal = decimal + 2**power
        power = power - 1
    return decimal

        
def decimalToBinary(decimal):
    power = 7
    binary = ""
    for i in range(8):
        if decimal >= 2**power:
            binary = binary + "1"
            decimal = decimal - (2**power)
        else:
            binary = binary + "0"
        power -= 1
    return binary

def rotateRight(inputString):
    last = inputString[len(inputString) - 1]
    string = last + inputString[:len(inputString) -1]
        
    return string
    


def checkSumR(inputString):
    checkSum = 0
    i = 0
    
    if len(inputString) % 2 == 1:
        inputString = inputString + " "
    while i < len(inputString) - 1:
        firstLetter = inputString[i]
        secondLetter = inputString[i + 1]
        a1 = ord(firstLetter)
        a2 = ord(secondLetter)
        b1 = decimalToBinary(a1)
        b2 = decimalToBinary(a2)
        binary = b1 + b2
        rotation = rotateRight(binary)
        decimal = binaryToDecimal(rotation)
        checkSum = checkSum + decimal
        i = i + 1
            
    checkSum = checkSum % (2**16)
    return checkSum
