#Evan Carnevale
#CSC 110 - Survey of Computer Science
#Professor Albluwi
#Homework 2 - Problem 2

number1 = float(input("Enter a number"))
number2 = float(input("Enter another number"))

if number1 > 0 and number2 > 0:
    print("The sum of the two numbers is:", number1 + number2)
elif number1 < 0 and number2 <0:
    print("The product of the two numbers is:", number1 * number2)
elif number1 == 0 or number2 == 0:
    print("Error")
else:
    print("The value of the second number subtracted from the first number then divided by 2 is:", (number1 - number2)/2)
    
