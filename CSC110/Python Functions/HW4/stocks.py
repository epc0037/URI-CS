# Evan Carnevale
# CSC 110 - Survey of Computer Science
# Professor Albluwi
# Homework 4 - Problem 1
# This program will get create two lists for stock names and prices,
# which will be entered by the user using a loop. I will utilize 3 functions:
# the main function, the searchStock function and the printStock function.

def main():
    # Create two empty lists for stock names and prices
    stockNames = []
    stockPrices = []

    # variable to control the loop
    end = "continue"

    while end != "done":
        #Get the stock name and prices
        name = str(input("Enter the stock name you wish to add to the list: "))
        price = int(input("Enter the price of the stock you added to the list: "))
        print("\n")

        # Append the name and prices to the lists
        stockNames.append(name)
        stockPrices.append(price)

        # Prompt the user to continue the loop
        print("If you wish to stop adding stocks, enter 'done' ")
        end = str(input("Type 'continue' to add more stocks: "))
        print("\n")

    # Prompt the user to find a stock with its corresponding price in the list using functions
    s = str(input("Enter a stock name you wish to search for in order to see which stocks are higher: "))
    p = searchStock(s, stockNames, stockPrices)
    printStock(p, stockNames, stockPrices)

# Function that returns the price of the searched stock
# I found an issue here at first in my code. I had an if-else statement
# but I realized I did not need the else, rather to just pull out the return
# and keep the indent even with the for loop. This seemed to solve my issue with
# the loop because it would return -1 when I wanted it to return the price from
# the stockPrices list.
def searchStock(s, stockNames, stockPrices):
    for i in range(len(stockNames)):
        if stockNames[i] == s:
            return stockPrices[i]
    return -1

# Function that prints all the stocks above the value of the searched stock
def printStock(p, stockNames, stockPrices):
    for i in range(len(stockPrices)):
        if stockPrices[i] > p:
            print(stockNames[i])
        else:
            print()
            

main()

        
