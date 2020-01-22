# Evan Carnevale
# Professor Albluwi
# CSC 110 - Survey of Computer Science (Section 1)
# Due Date: May 2nd, 2016 (Last Day of Classes @ 11:55pm !!)
# Programming Project Implementation : The Game of Mastermind
# -This program will play the game of Mastermind where the computer
#  chooses the hidden colors, and the human player attempts to guess the hidden colors.
# --I will utilize 4 functions to the play the Mastermind game including:
# 1) generateRandomColorsList() - randomly chooses 4 out of the 6 colors and stores them in a list
# 2) generateClueList() - based on the human's guess, this will generate a clue list displayed back to the human
# 3) generateGuess() - This is where the user will input their guess of the 4 random colors
# 4) main() : displays the menu and implements all of the above functions.

import random

ALL_COLORS_LIST = ['red','orange','yellow','green','blue','purple']

def generateRandomColorsList():
    Color_List = []
    i = 0
    while i < 4:
        color = random.randint(0,5)
        Color_List.append(ALL_COLORS_LIST[color])
        i = i + 1
    return Color_List

def generateClueList(random_color_list, guess):
    Clue_List = []
    tempList = list(random_color_list)
    for i in range(4):
        if guess[i] == tempList[i]:
            if Clue_List == []:
                Clue_List += ['2']
            tempList[i] = 'MATCH'
    for j in range(4):
        for k in range(4):
           if guess[j] == tempList[k]:
               if '1' not in Clue_List:
                   Clue_List += ['1']
               tempList[k] = 'MATCH'
    tempList = list(random_color_list)
    return Clue_List
    
def generateGuess():
    Guess_List = []
    
    print("Make a guess of four colors: \n \n 0 - Red \n 1 - Orange \n"
          " 2 - Yellow \n 3 - Green \n 4 - Blue \n 5 - Purple \n"
          "-------------------------------------------------- \n")
    
    guess1 = int(input("1) Guess the first color: "))
    guess2 = int(input("2) Guess the second color: "))
    guess3 = int(input("3) Guess the third color: "))
    guess4 = int(input("4) Guess the fourth color: "))
    Guess_List.append(ALL_COLORS_LIST[guess1])
    Guess_List.append(ALL_COLORS_LIST[guess2])
    Guess_List.append(ALL_COLORS_LIST[guess3])
    Guess_List.append(ALL_COLORS_LIST[guess4])
        

    print("\n Your guess is: ")
    print(Guess_List)
    return Guess_List

def main():
    NEXT_GUESS = 0
    print("Welcome to the Mastermind Game! \n \n The Rules: \n \n -The computer will randomly chose" 
          " colors from the list of red, orange, yellow, green, blue and purple. The codebreaker (YOU!!)"
          " will have 10 chances to guess the EXACT order of the colors (& colors may repeat!). \n \n"
          "After each incorrect guess, a clue list will be generated. \n -- If the guess has a correct"
          " color in the correct position, a 2 will be displayed, \n -- If the guess has a correct color,"
          " but in the wrong position, a 1 will be displayed. \n -- If nothing is displayed, then you must"
          " try your best to guess again! \n\n Guess the right order of the colors & you win!!! \n")
    
    selection = str(input("Do you Wish to Play? \n"))
    selection = selection.lower()
    if selection == "no" or selection == "n":
        return "Thanks Anyways!"
    else:
        print(" OK -- Let's Play!!!! \n \n")
        random_color_list = generateRandomColorsList()
        guess = generateGuess()
        print(random_color_list)
        
        while NEXT_GUESS < 9:
            NEXT_GUESS += 1
            clue = generateClueList(random_color_list, guess)
            print('\n The Clue is: ', clue, '\n')
            print(random_color_list)
            print("\n Reminder: \n 1 = correct color, wrong position \n 2 = correct color, correct position \n \n")
            print("You have guessed: ", NEXT_GUESS , " times")
            guess = generateGuess()
            if guess == random_color_list:
                return "Congradulations!! you guessed the correct list: ", random_color_list
    return "The random color list was : ", random_color_list
