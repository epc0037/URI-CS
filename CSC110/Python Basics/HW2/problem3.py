#Evan Carnevale
#CSC 110 - Survey of Computer Science
#Professor Albluwi
#Homework 2 - Problem 3

TOTAL_BUGS = 0
DAYS = 1

while DAYS <= 7:
    print("Day", DAYS, ": Did you collect a lot of bugs today?")
    today_bug = int(input("Enter the number of bugs collected today"))
    TOTAL_BUGS += today_bug
    DAYS +=1
    print('\n')

print("The total number of bugs collected in the week:", TOTAL_BUGS, "bugs.")
