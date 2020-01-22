# Evan Carnevale
# CSC 110 - Survey of Computer Science
# Professor Albluwi
# Homework 5 - Olympic Games
# This program will utilize three functions and one file "olympics.txt'
# The user will enter the file name, which will be passed to the readData function
# This function will put the years and locations into separate lists where both
# will be printed to the terminal.
# The user will be prompted to enter a year, which will be passed to the findLoc function
# along with the year and location lists. Finally, the found location and year will be printed to the screen.

# The readData function reads the contents of a given file , splits the contents on a given character, and stores each
# of these variables into separate lists. These lists are returned at the end of the function
def readData(filename):
    inputFile = open(filename, 'r')
    yearList = []
    locList = []
    line = inputFile.readline()
    while line != '' :
        line = line.strip()
        year, location = line.split('\t')
        yearList = yearList + [year]
        locList = locList + [location]
        line = inputFile.readline()
    inputFile.close()
    return yearList, locList

# the findLocation function finds the location of the Olympics for a given year and has 3 parameters passed to it,
# the yearList, locList, and the year the user wishes to search for.
# The corresponding location is returned or if it is not in the list, "Not Found" is returned
def findLocation(yearList, locList, year):
    found_location = 0
    i = 0
    while found_location == 0 and i < len(locList):
        if year == yearList[i]:
            found_location = 1
        else:
            i = i + 1
    if found_location == 0:
        location = 'Not Found'
    else:
        location = locList[i]
    return location

# The main function prompts the user to enter the file name, executes the readData function and stores the returned values
# into yearList and locList and prints them to the screen. Next, the user is prompted to enter a year they wish to search for.
# The findLocation function is then executed and the returned location is stored in the variable "location".
# Finally, the year and location of that specific Summer Olympic games is displayed to the user.
def main():
    fileName = input("Enter the file name here please: ")
    yearList, locList = readData(fileName)
    print("The year list is:", '\n',yearList)
    print('\n')
    print("The location list is:",'\n', locList)
    print('\n')
    year = input("Enter the year you wish to see where the Olympics were held: ")
    location = findLocation(yearList, locList, year)
    print("The Summer Olympics of", year, "was held in", location)
    
