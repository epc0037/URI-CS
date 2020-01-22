# CSC 110 (Section 1) - Spring 2016
# Week 7: Analysis of Algorithms
# Homework 7 - Problem 1
# Evan Carnevale - 100460662

# This function reads the data from the file and creates three empty lists
# for the lines in the file, each will be split into three variables
# including year, city and country (a temp variable 'place' was also used)
# each of these values were then added to the corresponding list
# and each list was returned.
def readData(filename):
    inFile = open(filename,'r')
    years = []
    cities = []
    countries = []
    line = inFile.readline()
    while line != '':
        year, place = line.split('\t')
        city, country = place.split(',')
        country = country.strip()
        years = years + [int(year)]
        cities = cities + [city]
        countries = countries + [country]
        line = inFile.readline()
    inFile.close()
    return years, cities, countries

# This function does a linear search through the yearsList and
# returns the number of times it compared the value you searched for
# in the list and it also returns the index of that value as well.
def findYearLinear(yearsList, year):
    counter = 0
    index = 0
    found = False

    while index < len(yearsList) and not found:
        if int(year) == yearsList[index]:
            counter = counter + 1
            found = True
        else:
            counter = counter + 1
            index = index + 1
            
    print('Linear search took: ', counter)
    return index
    
    
# This function does a binary search through the yearList and
# returns the index of the year you search for as well as the number of
# comparisons that were made by the function.
#*****NOTE: I started my counter at 1 instead of 0 so I might
# have returned the number of comparisons off by 1 value.
def findYearBinary(yearList, year):
    counter = 1
    start = 0
    end = len(yearList)
    
    startMarker = start
    endMarker = end
    
    while (endMarker - startMarker) != 1:
        middleMarker = (endMarker + startMarker) // 2
        if int(year) < yearList[middleMarker]:
            counter = counter + 1
            endMarker = middleMarker
        elif int(year) > yearList[middleMarker]:
            counter = counter + 1
            startMarker = middleMarker
        elif int(year) == yearList[middleMarker]:
            print('Binary search took: ', counter)
            return middleMarker

    middleMarker = (endMarker + startMarker) // 2
    if int(year) == yearList[middleMarker]:
        print('Binary search took: ', counter)
        return middleMarker
    return ''
        
    
#----------------------------------------------------12
# These functions are provided for you - DONT CHANGE

# given a year, find the city in which the olypmics was held
# you can either search by linear of binary search algorithms
def findCity(year, yearList, cityList, searchMode):
    if searchMode == 'linear':
        index = findYearLinear(yearList, year)
        if index != -1:
            return cityList[index]
        else:
            return 'Year Not Found'
    elif searchMode == 'binary':
        index = findYearBinary(yearList, year)
        if index != -1:
            return cityList[index]
        else:
            return 'Year Not Found'
    else:
        return 'illegal search mode'
    
# this does the same thing as findCity, except the variable name is different
def findCountry(year, yearList, countryList, searchMode):
    return findCity(year, yearList, countryList, searchMode)

def printMenu():
    print('Select one of the following choices:')
    print('\t1- Find City - Search Using Linear Search ')
    print('\t2- Find City - Search Using Binary Search ')
    print('\t3- Find Country - Search Using Linear Search ')
    print('\t4- Find Country - Search Using Binary Search ')
    print('\t5- Exit \n')

def main():
    filename = input('Enter name of file: ')
    years, cities, countries = readData(filename)

    choice = 1
    while choice != 5:
        printMenu()
        choice = int(input())
        if choice == 5:
            print('Good Bye')
            break
        else:
            year = input('Enter a year: ')
            if choice == 1:
                city = findCity(year, years, cities, 'linear')
                print('The Olympics in ', year, ' was held in : ', city, '\n')
            elif choice == 2:
                city = findCity(year, years, cities, 'binary')
                print('The Olympics in ', year, ' was held in : ', city, '\n')
            elif choice == 3:
                country = findCountry(year, years, countries, 'linear')
                print('The Olympics in ', year, ' was held in : ', country, '\n')
            elif choice == 4:
                country = findCountry(year, years, countries, 'binary')
                print('The Olympics in ', year, ' was held in : ', country, '\n')
            else:
                print('Wrong choice! Try again.\n')
