# Evan Carnevale & Jesus Lopez
# Lab 14: Computer Architecture

import gates1

def halfAdder(A,B):
    CarryOut = A and B
    Sum = gates1.xor(A,B)
    return int(Sum), int(CarryOut)

def fullAdder(A,B,CarryIn):
    Sum1, CarryOut1 = halfAdder(A,B)
    Sum, CarryOut2 = halfAdder(Sum1,CarryIn)
    CarryOut = CarryOut1 or CarryOut2
    return int(Sum), int(CarryOut)

def fourBitAdder(A,B):
    a = A[::-1]
    b = B[::-1]

    sum0, carryOut1 = halfAdder(b[0],a[0])
    sum1, carryOut2 = fullAdder(b[1],a[1],carryOut1)
    sum2, carryOut3 = fullAdder(b[2],a[2],carryOut2)
    sum4, sum3 = fullAdder(b[3],a[3],carryOut3)

    result = str(sum0) + str(sum1) + str(sum2) + str(sum3) + str(sum4)
    result = result[::-1]
    return result
    
