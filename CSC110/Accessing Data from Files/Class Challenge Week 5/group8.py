# Group 8
# Secret Code

def getPasswordLetter(fileName, line_number, ch):
    inFile = open(fileName , 'r')
    for i in range(line_number):
        line = inFile.readline()
        letter = line[ch]
        

    
    inFile.close()
    return letter

def getPassword():
    fileName = input("Enter the file name: ")
    password = []
    counter = 0
    while counter < 12:
        line = int(input("Enter the line number: "))
        position = int(input("Enter the position: "))

        reading = getPasswordLetter( fileName, line, position)

        password = password + [reading]
        counter = counter + 1
        
    return password

def decryptLetter(letter, fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    ch1, ch2 = line.split('-')
    while letter != ch1:
        line = inFile.readline()
        ch1, ch2 = line.split('-')
    return ch2.strip()
    inFile.close()

def decrypt(secret_msg, fileName):
    message = []
    for i in range(len(secret_msg)):
        letter = decryptLetter(secret_msg[i], 'group8_CodeSheet.txt')
        message = message + [letter]
    return message
        
        
    



