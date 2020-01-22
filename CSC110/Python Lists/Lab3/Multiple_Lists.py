# Evan Carnevale & Ronin Soto
# Professor Albluwi
# CSC 110
# February 12th, 2016
# Lab 3 - Part 2

# Stock names and prices
stocks = ['IBM', 'AAPL', 'GOOG', 'FB', 'SMSN', 'INTC', 'MCD', 'TWTR']
Prices = [23.4, 24.5, 25.3, 56.7, 89.4, 45.3, 43.6, 67.4]

# User input for the stock name
stock_name = str(input("Enter the name of the stock: "))

# global percentage converted into a decimal for calculations
PERCENTAGE = int(input("Enter the percentage increase of that stock: "))
DECIMAL = PERCENTAGE / 100

# loop thru our stocks to match indexs between stocks and Prices
for i in range(len(stocks)):
    if stocks[i] == stock_name:
        Prices[i] = Prices[i] + DECIMAL * Prices[i]
        
# Output for the user
print(Prices)
    
    
