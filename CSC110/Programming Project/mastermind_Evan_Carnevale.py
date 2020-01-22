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

# import the random module -- this will help generate a random color lists
import random


# global colors list
ALL_COLORS_LIST = ['red','orange','yellow','green','blue','purple']


# function that will create a random color list
def generateRandomColorsList():
    # empty color list
    Color_List = []
    # counter
    i = 0
    # loop will counter is less than 4...
    while i < 4:
        # generates a random number between 0 and 5
        color = random.randint(0,5)
        # appends the color from the global color list to the empty list
        Color_List.append(ALL_COLORS_LIST[color])
        # increment counter
        i = i + 1
    # output - return Color_list
    return Color_List


# function that will generate the clue list
def generateClueList(random_color_list, guess):
    # new list for writing clues
    Clue_List = []
    # temp list to alter color list without changing it
    temp_list = list(random_color_list)
    # looping through color list...
    for i in range(len(random_color_list)):
            # if the guess is anywhere in color list...
            if guess[i] ==  temp_list[i]:
                # if they are in the same position..
                if Clue_List == []:
                    # add a 2 to the clue list
                    Clue_List += [2]
                    # don't match this one again
                temp_list[i] = 'MATCH'
    # loop through random color list...
    for j in range(len(random_color_list)):
        # loop through guess list...
        for k in range(len(guess)):
                # if not the same position..
                if guess[j] == temp_list[k] and j != k:
                    # if 1 not already in the clue list..
                    if 1 not in Clue_List:
                        # add 1
                        Clue_List += [1]
                    # don't match this one again
                    temp_list[k] = 'MATCH'
    # revert temp list back to original random color list
    temp_list = list(random_color_list)
    # output - return Clue_list
    return Clue_List


# function that will allow the user to generate their guess
def generateGuess():
    # create an empty guess list
    Guess_List = []
    # output displayed to the user
    print("Make a guess of four colors: \n \n 0 - Red \n 1 - Orange \n"
          " 2 - Yellow \n 3 - Green \n 4 - Blue \n 5 - Purple \n"
          "-------------------------------------------------- \n")
    # guesses 1-4 (only accepts integer values)
    guess1 = int(input("1) Guess the first color: "))
    guess2 = int(input("2) Guess the second color: "))
    guess3 = int(input("3) Guess the third color: "))
    guess4 = int(input("4) Guess the fourth color: "))
    # appends the correct color depending upon user's guesses
    Guess_List.append(ALL_COLORS_LIST[guess1])
    Guess_List.append(ALL_COLORS_LIST[guess2])
    Guess_List.append(ALL_COLORS_LIST[guess3])
    Guess_List.append(ALL_COLORS_LIST[guess4])

    # output displayed the user
    print("\n Your guess is: ")
    print(Guess_List)
    # output - return the guess list
    return Guess_List


# main function - implements all aobve functions
def main():
    # local guess variable
    NEXT_GUESS = 0
    # output displayed to the user - The Rules of Mastermind!!
    print("Welcome to the Mastermind Game! \n \n The Rules: \n \n -The computer will randomly chose" 
          " colors from the list of red, orange, yellow, green, blue and purple. The codebreaker (YOU!!)"
          " will have 10 chances to guess the EXACT order of the colors (& colors may repeat!). \n \n"
          "After each incorrect guess, a clue list will be generated. \n -- If the guess has a correct"
          " color in the correct position, a 2 will be displayed, \n -- If the guess has a correct color,"
          " but in the wrong position, a 1 will be displayed. \n -- If nothing is displayed, then you must"
          " try your best to guess again! \n\n Guess the right order of the colors & you win!!! \n")

    # prompts the user to see if they want to play the game
    selection = str(input("Do you Wish to Play? \n"))
    # turns that input into all lowercase characters
    selection = selection.lower()
    # if the user says they don't want to play..
    if selection == "no" or selection == "n":
        # output - goodbye!!!
        return "Thanks Anyways!"
    # everything else besides a no..
    else:
        # output displayed to the user
        print(" OK -- Let's Play!!!! \n \n")
        # function call - generates the random color list
        random_color_list = generateRandomColorsList()
        # function call - generates the user's guess
        guess = generateGuess()
        # looping while the user has more turns left...
        while NEXT_GUESS < 9:
            # increment next guess for the first guess above
            NEXT_GUESS += 1
            # function call - display the clue
            print('\n The Clue is: ', generateClueList(random_color_list, guess), '\n')
            # output - display the clue key again
            print("\n Reminder: \n 1 = correct color, wrong position \n 2 = correct color, correct position \n \n")
            # output - display how many times the user has made a guess
            print("You have guessed: ", NEXT_GUESS , " times")
            # function call - user makes the next guess
            guess = generateGuess()
            # if the guess list is the same as the random color list..
            if guess == random_color_list:
                # YOU WIN!!!!!
                return "Congratulations!! you guessed the correct list: ", random_color_list
    # you lost :(
    return "The random color list was : ", random_color_list
        
