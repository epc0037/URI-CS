#Evan Carnevale
#CSC110 - Survey of Computer Science
#Professor Albluwi
#This program is designed to compute sales tax
#for purchases made in August 2014. The sales tax is 6% of the
#sale and the sale value will be stored as a variables of type float.
#Finally, the program will display a message displaying the sales tax for August 2013.

#global variable
SIXPERCENT= .06

#user input - total sales for month of August
sale_value = float(input("Enter the value of the company's sales in dollars in August 2014: "))

#calculations for sales tax
sales_tax = sale_value * SIXPERCENT

#output statement
print("The sales tax is $",format(sales_tax, '.2f'),"for August 2013")
