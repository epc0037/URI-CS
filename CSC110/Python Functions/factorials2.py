# CSC 110 - Spring 2016 - Section 1
# Week 4 (Functions) - Class Activities (Tuesday)
# Examples: Combinations

# This program computes n choose r (n | r)
# (n | r) = n!/((n-r)!*r!)

# Solution 2 using functions

# factorial function
def fact(number):
    fact = 1
    i = 1
    while i <= number:
        fact = fact*i
        i = i + 1
    return fact

# main program
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

result = fact(n) / (fact(n-r) * fact(r))
print(result)

