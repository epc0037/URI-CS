# Danielle Zaloudek
# Group 8
# Week 5 Challenge Secret Code


# Function to get password letter
def getPasswordLetter(fileName, line_number, ch):

    # Open file
    inFile = open(fileName , 'r')

    # For i in the line
    for i in range(line_number):
        line = inFile.readline()

        # Letter becomes character in line
        letter = line[ch]
        
    # Close file
    inFile.close()

    # Return the letter
    return letter


# Function to get whole password
def getPassword():
    fileName = input("Enter the file name: ")

    # Initialize empty password list
    password = []
    counter = 0

    while counter < 12:
        line = int(input("Enter the line number: "))
        position = int(input("Enter the position: "))
        
        # Pass fileName, line and position of letter to getPasswordLetter function
        reading = getPasswordLetter( fileName, line, position)
        
        
        # Add letters to password list
        password = password + [reading]
        counter = counter + 1
        
    # Return the full password   
    return password


# Function to decrypt letter
def decryptLetter(letter, fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()

    # Split into two characters
    # ch1 is letter we give, ch2 is letter we need
    ch1, ch2 = line.split('-')

    # While the letter doesn't equal ch1
    while letter != ch1:

        # Read next line
        line = inFile.readline()
        ch1, ch2 = line.split('-')
        
    # If letter equals ch2, return it  
    return ch2.strip()
    inFile.close()


# Function to decrypt full secret message
def decrypt(secret_msg, fileName):

    # Initialize empty message list
    message = []
    
    for i in range(len(secret_msg)):

        # Give decryptLetter the letter of secret_message to decode
        # Save result in letter
        letter = decryptLetter(secret_msg[i], 'group8_CodeSheet.txt')

        # Add all letters to message list for complete message
        message = message + [letter]

    # Return complete secret message    
    return message
        
        
    



