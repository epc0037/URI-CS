# CSC 110 - Fall 2013 (Section 2)
# Week 6 - Writing Programs


# Read from a file a library database
# Return a library catalogue
# The Catalogue is a list consisting of the following sublists:
# 1- Book Title List
# 2- Author List
# 3- Publishing Year List
# 4- Publisher List
def loadLibrary(filename):
    titleList = []
    authorList = []
    yearList = []
    publisherList = []
    inputFile = open(filename,'r')
    reading = inputFile.readline()
    while reading != '':
        reading = reading.strip()
        title, author, year, publisher = reading.split('-')
        titleList = titleList + [title]
        authorList = authorList + [author]
        yearList = yearList + [year]
        publisherList = publisherList + [publisher]
        reading = inputFile.readline()
    inputFile.close()
    catalogue = [titleList, authorList, yearList, publisherList]
    return catalogue

# Get a list of numbers as strings and convert to integers
def string_to_int(numberList):
    for i in range(len(numberList)):
        numberList[i] = int(numberList[i])
    return numberList


# ------------------ Search Functions ---------------------
# given a library catalogue, return record number (index)
def getRecord(catalogue, index):
    if index >= len(catalogue[0]) or index < 0:
        return -1 # Record not found
    else:     
        title = catalogue[0][index]
        author = catalogue[1][index]
        year = catalogue[2][index]
        publisher = catalogue[3][index]
        record = [title, author, year, publisher]
    return record

# Search a cataogue by a given string
# if mode = 0 --> search by title
# if mode = 1 --> search by author
# if mode = 2 --> search by publishing year
# if mode = 3 --> search by publisher
def search(catalogue, keyword, mode):
    for i in range(len(catalogue[0])):
        if(keyword == catalogue[mode][i]):
            return i
    return -1 # not found

# --------------- Printing Functions ------------------
# Print Full Library Catalogue
def printCatalogue(catalogue):
    printHeader()
    for i in range(len(catalogue)+1):
        record = getRecord(catalogue, i)
        printRecord(record)
    return

def printHeader():
    print("\nTitle\t\t\t Author\t\t\t Year\tPublisher")
    print("-------------\t\t ---------\t\t ----\t --------")

def printRecord(record):
    print(record[0].ljust(20), '\t', record[1].ljust(18),'\t',
              record[2].ljust(4), '\t', record[3])
    
# ----------------- Menues -----------------------------
def printMainMenue():
    print("\n")
    print("*********** Main Menue *************")
    print("1- Browse Library Catalogue")
    print("2- Search By Record Number")
    print("3- Search By Book Title")
    print("4- Search By Book Author")
    print("5- Search By Publishing Year")
    print("6- Search By Publisher")
    print("7- Exit")
    print("************************************")
    print("\n")

def getRecordMenue(catalogue):
    number = int(input("Enter Record Number: "))
    record = getRecord(catalogue, number)
    if (record == -1):
        print("No record found matching your search criteria!")
    else:
        printHeader()
        printRecord(record)
        
def searchByTitleMenue(catalogue):
    title = input("Enter Book Title: ")
    number = search(catalogue, title, 0)
    record = getRecord(catalogue, number)
    if (record == -1):
        print("No record found matching your search criteria!")
    else:
        printHeader()
        printRecord(record)
        
def searchByAuthorMenue(catalogue):
    author = input("Enter Author: ")
    number = search(catalogue, author, 1)
    record = getRecord(catalogue, number)
    if (record == -1):
        print("No record found matching your search criteria!")
    else:
        printHeader()
        printRecord(record)

def searchByYearMenue(catalogue):
    year = input("Enter Publishing Year: ")
    number = search(catalogue, year, 2)
    record = getRecord(catalogue, number)
    if (record == -1):
        print("No record found matching your search criteria!")
    else:
        printHeader()
        printRecord(record)

def searchByPublisherMenue(catalogue):
    publisher = input("Enter Publisher: ")
    number = search(catalogue, publisher, 3)
    record = getRecord(catalogue, number)
    if (record == -1):
        print("No record found matching your search criteria!")
    else:
        printHeader()
        printRecord(record)

def welcome():
    print("\n")
    print(" #########################################")
    print(" ##   Welcome to the X World Library    ##")
    print(" #########################################")
    print("\n")
    
def goodbye():
    print("\n")
    print(" #########################################")
    print(" ## Thank you for visiting our Library! ##")
    print(" ##     We Hope to See you Again!       ##")
    print(" #########################################")
    print("\n")
    
# ---------------- Main Function -----------------------
def main():
    catalogue = loadLibrary('libraryDB.txt')
    choice = 0
    welcome()
    while choice != 7:
        printMainMenue()
        choice = int(input("Please select a choice from the above menue: "))
        if choice == 1:
            printCatalogue(catalogue)
        elif choice == 2:
            getRecordMenue(catalogue)
        elif choice == 3:
            searchByTitleMenue(catalogue)
        elif choice == 4:
            searchByAuthorMenue(catalogue)
        elif choice == 5:
            searchByYearMenue(catalogue)
        elif choice == 6:
            searchByPublisherMenue(catalogue)
        elif choice == 7:
            goodbye()
            break
        else:
            print("Please Enter a valid choice")
    

