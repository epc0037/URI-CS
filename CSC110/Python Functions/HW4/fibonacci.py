# Evan Carnevale
# CSC 110 - Survey of Computer Science
# Professor Albluwi
# Homework 4 - Problem 2
# This program will utilize the Fibonacci sequence through functions and lists.

def main():
    # Prompt the user to see which nth term they wish to see
    n = int(input("Enter a number for the Fibonacci Sequence: "))
    # Output prints the list to the user.
    print(fibonacci(n))

    print("\n")
    print("Tests for values n =4, 10 and -4:" + "\n")
    print("Test n=4: ", fibonacci(4))
    print("Test n=10: ", fibonacci(10))
    print("Test n=-4: ", fibonacci(-4))
    


# Define the fibonacci function using a, b and a temporary variable.
def fibonacci(n):
    # Eliminates output for anything less than or equal to 0
    if n<= 0:
        return []
    
    # Fibonacci Sequence
    a = 0
    b = 1
    fib = []
    fib.append(a)
    i = 0
    # Loop that appends the values to the list and removes the last value.
    # I needed to remove the last value because it was printing one sequence too many.
    for i in range(0,n):
        temp = a
        a = b
        b = temp + b
        fib.append(a)
        i += 1
    fib.pop(-1)
    return fib

main()
