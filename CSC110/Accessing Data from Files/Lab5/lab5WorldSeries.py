# CSC110 - Spring 2015, Section 3
# Week 6: Python Files
# World Series Results
# Student Name: ____________ and ID: ______________

#---------------------------------------------------

# Given a file with the World Series Champions since 1904
# Allow user to ask various questions about the results

#---------------------------------------------------
#                           PART B
# This function will read the data from the input file ("worldseries.txt")
# The function takes no input parameters
# The function returns three lists: the list of years, the list of winnners and the list of losers

def getChamps():

    # initialize three lists
    yearList = []
    winnerList = []
    loserList = []

    # Add your code here
    fileName = input("Enter the file name: ")
    inFile = open(fileName, 'r')
    line = inFile.readline()
    line = line.strip()
    while line != '':
        year, winner, loser = line.split(',')
        yearList = yearList + [year]
        winnerList = winnerList +[winner]
        loserList = loserList + [loser]
        line = inFile.readline()
        line = line.strip()

    inFile.close() 

    
    # return the three lists
    return yearList, winnerList, loserList

#---------------------------------------------------
#                           PART C
# This function will take three input parameters:
# a year to search for
# the yearList
# the winnerList
# the function searchs for the requested year in the yearList and
# returns the corresponding winner from the winnerList
def findWinner(year, yearList, winnerList):

    for i in range(len(yearList)):
        if yearList[i] == year:
            return winnerList[i]
    return "No winner."

#---------------------------------------------------
#                           PART D
# This function will take three input parameters:
# a year to search for
# the yearList
# the loserList
# the function searchs for the requested year in the yearList and
# returns the corresponding winner from the winnerList

def findLoser(year,yearList, loserList):
    for i in range(len(yearList)):
        if yearList[i] == year:
            return loserList[i]
    return "No loser."
            

#---------------------------------------------------
#                           PART E
# This function will take two input parameters:
# a team and the winner list.
# It will count the number of times that team has won the World Series
# It should return the number of times the team has won the world series

def countWins(team, winnerList):
    numWins = 0
    for i in range(len(winnerList)):
        if team == winnerList[i]:
            numWins += 1
    
    return numWins

#---------------------------------------------------
#                       EXTRA CREDIT
#This function finds out who won the most World Series

def mostWinners(winnerList,loserList):
    overallCounter = 0
    overallTeam = ""
    for team in winnerList: #For each winner in the list...
        teamCounter = 0
        for game in winnerList: #Count how many times that winner won
            if game == team:
                teamCounter+=1
        if teamCounter >= overallCounter: #If they won more than the previous max, overwrite it
            overallCounter = teamCounter
            overallTeam = team

    print("The "+overallTeam+" have won the World Series the most times, at "+str(overallCounter)+" victories.")

    overallCounter = 0
    overallTeam = ""
    for team in loserList: #For each loser in the list...
        teamCounter = 0
        for game in loserList: #Count how many times that loser lost
            if game == team:
                teamCounter+=1
        if teamCounter >= overallCounter: #If they lost more than the previous max, overwrite it
            overallCounter = teamCounter
            overallTeam = team

    print("The "+overallTeam+" have lost the World Series the most times, at "+str(overallCounter)+" defeats.")

#---------------------------------------------------
#               DON'T EDIT THESE FUNCTIONS
def getChoice():
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    print("")
    print("Make a selection from the following choices:")
    print("1 - Find the World Series Winner for a particular year")
    print("2 - Find the World Series Loser for a particular year")
    print("3 - Count how many times a team has won the World Series")
    print("4 - Quit")
    choice = int(input("Enter your choice --> "))
    print("")
    return choice

def main():
    yearList, winnerList, loserList = getChamps()
    choice = getChoice()
    while choice != 4:
        if choice == 1:
            year = input("Enter the year to search for: ")
            winner = findWinner(year, yearList, winnerList)
            print("The winner for that year was ", winner)
            choice = getChoice()
        elif choice == 2:
            year = input("Enter the year to search for: ")
            loser = findLoser(year, yearList, loserList)
            print("The loser for that year was ", loser)
            choice = getChoice()
        elif choice == 3:
            team = input("Enter the team name: ")
            wins = countWins(team,winnerList)
            print("Your team won the World Series ", wins, " times.")
            choice = getChoice()
        else:
            print("Error in your choice")
            choice = getChoice()
    print("Good-bye")
    
