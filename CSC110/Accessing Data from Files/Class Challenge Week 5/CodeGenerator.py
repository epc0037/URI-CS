# CSC 110 Section 2, Fall 2013
# Week 5 - Challenge
# Written by: Qutaiba Albluwi

def getCodeSheet(key1, key2,groupNumber):
    fileName = 'group'+str(groupNumber)+'_CodeSheet.txt'
    secretTableFile = open(fileName, 'w')

    alphabet = getAlphabet()
    cipherbet = []

    for i in range(26):
        cipher = decrypt(alphabet[i],key1,key2)
        secretTableFile.write(alphabet[i])
        secretTableFile.write('-')
        secretTableFile.write(cipher)
        secretTableFile.write('\n')
    
    secretTableFile.close()
    print("The Code Sheet was successfully generated! Check your directory")

def decrypt(ciphertext, key1, key2):
    ciphertext = ciphertext.upper()
    ciphertext = list(ciphertext)

    plaintext = []
    for i in range(len(ciphertext)):
        plain = charValue(ciphertext[i])
        plain = (plain - key2)%26
        plain = (plain * inverse(key1,26))%26
        plaintext = plaintext + [plain]

    for j in range(len(plaintext)):
        plaintext[j] = getChar(plaintext[j])

    return listToString(plaintext)

# find inverse
def inverse(number,mod):
    for i in range(mod):
        if (number*i)%mod == 1:
            return i
    return "UN" #undefined


# Given a character, Find its index in alphabet
def charValue(character):
    alphabet = getAlphabet()
    if (str(character).isalpha()):
        return alphabet.index(character)
    else:
        return - 1

# Given a number find which letter it corresponds to
def getChar(index):
    alphabet = getAlphabet()
    if index >= 0 and index <26:
        return alphabet[index]
    else:
        return - 1

# Get alphabets in a list
def getAlphabet():
    return ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#listToString
# Takes a list of characters and convert it into a string
def listToString(stringList):
    outputString = ''
    outputString = outputString.join(stringList)
    return outputString
