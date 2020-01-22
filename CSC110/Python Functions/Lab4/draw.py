# Tic-Tac-Toe Game

def drawBoard(board):
    # Draws the board using the list of numbers
    print(" ")
    print(" ",board[0]," | ",board[1]," | ", board[2])
    print("----------------")
    print(" ",board[3]," | ",board[4]," | ", board[5])
    print("----------------")
    print(" ", board[6]," | ",board[7]," | ", board[8])
    print(" ")
    return

def nextMove(turn,bd):
    # Input:  turn - "O" or "X" depending on whose turn it is
    # Output: bd - the updated board with the new move inserted

    # Asks the player to choose a spot on the board
    # The turn parameter represents the player ("O" or "X")
    # Replace the spot on the board with the right symbol
    # Return the board
    
    spot = int(input("Enter a position on the board you wish to place your move."))
    bd[spot] = turn
    return bd
              

def isWinner(bd):
    # Input: bd - the current board
    # Output: the winner of the game ("X" or "O"), if one exists, otherwise "none"
 
    # Determines if there is a winner 
    # If X is the winner, return "X"
    # If O is the winner, return "O"
    # If there is no winner, return "none"
    if bd[0] == bd[1] and bd[1]== bd[2]:
        return bd[0]
    elif bd[3] == bd[4] and bd[4]== bd[5]:
        return bd[3]
    elif bd[6] == bd[7] and bd[7]== bd[8]:
        return bd[6]
    elif bd[0] == bd[4] and bd[4]== bd[8]:
        return bd[0]
    elif bd[2] == bd[4] and bd[4]== bd[6]:
        return bd[2]
    elif bd[0] == bd[3] and bd[3]== bd[6]:
        return bd[0]
    elif bd[2] == bd[5] and bd[5]== bd[8]:
        return bd[2]
    else:
        return "none"

def moreMoves(bd):
    # Input: bd - the current board
    # Output: 1 if there are more moves left on the board, 0 if not

    # Determines if there are any moves left 
    # if any spaces are left to play
    # return 1 if there are any moves left
    # return 0 if there are no moves left

    for i in range(len(bd)):
        if bd[i] != 'X' or bd[i] != 'O':
            return 1
    return 0


def nextTurn(turn):
    # Input: turn - "O" or "X" depending on whose turn just finished
    # Output: "O" or "X" depending on whose turn is next

    # Determines whose turn it is based on whose turn 
    # just finished
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    return turn
              
# Main code
#
# Initialize the board with position numbers
# Start out with X going first
# Set the winner to 'none' to start
# As long as there is no winner and there are still moves to make, loop through the game
# Each time through the loop
#       Draw the board
#       Make the next move
#       Determine if there is a winner
#       Set the turn to the next player
#
# Once the loop is complete, display the board one more time and print the winner

def main():
    bd = [0,1,2,3,4,5,6,7,8]
    turn = 'X'
    winner = 'none'
    while winner == 'none' and moreMoves(bd)==1:
        drawBoard(bd)
        bd = nextMove(turn,bd)
        winner = isWinner(bd)
        turn = nextTurn(turn)

    drawBoard(bd)
    print("Player ",winner," is the winner")
