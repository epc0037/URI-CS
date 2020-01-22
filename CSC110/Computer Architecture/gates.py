# CSC 110: Spring 2016 (Section 1)
# Week 16: Computer Architecture
# Class Activities: Python Implementation of Logical Gates

# AND gate:
# 0 and 0 --> 0
# 0 and 1 --> 0
# 1 and 0 --> 0
# 1 and 1 --> 1
# Python has built-in function for AND gate (and)

# OR gate:
# 0 or 0 --> 0
# 0 or 1 --> 1
# 1 or 0 --> 1
# 1 or 1 --> 1
# Python has built-in function for OR gate (or)

# NOT gate
# not 0 --> 1
# not 1 --> 0
# Python has built in-function for NOT gate (not)

# XOR gate
# 0 xor 0 --> 0
# 0 xor 1 --> 1
# 1 xor 0 --> 1
# 1 xor 1 --> 0
def xor(a,b):
    if not a and b:
        return True
    if a and not b:
        return True
    return False

# NAND gate
# 0 nand 0 --> 1
# 0 nand 1 --> 1
# 1 nand 0 --> 1
# 1 nand 1 --> 0
def nand(a,b):
    return not (a and b)

# NOR gate
# 0 nor 0 --> 1
# 0 nor 1 --> 0
# 1 nor 0 --> 0
# 1 nor 1 --> 0
def nor(a,b):
    return not (a or b)

# XNOR gate
# XOR gate
# 0 xor 0 --> 1
# 0 xor 1 --> 0
# 1 xor 0 --> 0
# 1 xor 1 --> 1
def xnor(a,b):
    return not xor(a,b)
