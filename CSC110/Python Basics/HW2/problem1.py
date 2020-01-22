#Evan Carnevale
#CSC 110 - Survey of Computer Science
#Professor Albluwi
#Homework 2 - Problem 1

redButton = int(input("Enter integer value for redButton (1 or 0)"))
blueButton = int(input("Enter integer value for blueButton (1 or 0)"))

if redButton >= 2 or redButton < 0:
    print("Wrong input for redButton")
elif blueButton >= 2 or blueButton < 0:
    print("Wrong input for blueButton")
elif redButton == 1 and blueButton == 1:
    print("Switch on Machine 1")
elif redButton == 0 and blueButton == 0:
    print("All Machines are Off")
else:
    print("Switch on Machine 2")

print("Goodbye!")

