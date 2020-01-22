# Evan Carnevale
# Professor Albluwi
# CSC110 - Spring 2016
# Week 8: Cryptography
# When you decrypt the first message from the Caesar cipher, you  get 'secret'
# When you decrypt the second message from the Polyalphabetic cipher, you get 'jamesbond'

def caesar(plaintext,shift):  
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
    # initialize ciphertext as blank string
    ciphertext = ''
    # loop through the length of the plaintext
    for i in range(len(plaintext)):
        # get the ith letter from the plaintext
        letter = plaintext[i]
        # find the number position of the ith letter
        num_in_alphabet = alphabet.index(letter)
        # find the number position of the cipher by adding the shift
        cipher_num = (num_in_alphabet + shift) % len(alphabet)
        # find the cipher letter for the cipher number you computed
        cipher_letter = alphabet[cipher_num]
        # add the cipher letter to the ciphertext
        ciphertext = ciphertext + cipher_letter
    # return the computed ciphertext
    return ciphertext						

# The decryptC function takes the shift (integer) ciphertext (string) as arguments passed to the function
# the regular alphabet is stored in a list and the plaintext is initialized as a blank string.
# for each element in the ciphertext, i is equal to the index of that element subtracted
# by the shift, which we then take the modulus of. This results in the new letter shifted
# according to the new position in the alphabet, which is then added to the plaintext string
# and returned to the user.
def decryptC(shift, ciphertext):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    plaintext = ''
    for l in ciphertext:
        i = (alphabet.index(l) - shift) % 26
        plaintext = plaintext + alphabet[i]

    return plaintext.lower()


def polyalphabetic(plaintext,codeword):
    alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ciphertext = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter == ' ':
            ciphertext = ciphertext + letter
        elif letter in alphabet:
            num_in_alphabet = alphabet.index(letter)

            # Find the position in the codeword with the letter to shift
            shiftIndex = i % len(codeword)

            # Find the letter in the codeword to shift
            shiftLetter = codeword[shiftIndex]

            # Find the number associated with the letter to be used as the shift
            shift = alphabet.index(shiftLetter)

            cipher_num = (num_in_alphabet + shift) % len(alphabet)
            cipher_letter = alphabet[cipher_num]
            ciphertext = ciphertext + cipher_letter
        else:
            ciphertext = ciphertext + '_'
    return ciphertext

def decryptP(ciphertext, codeword):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    plaintext = ''
    # Loop through the length of the ciphertext
    for l in range(len(ciphertext)):
        # get the lth letter of the ciphertext
        letter = ciphertext[l]
        # Find the number position of the lth letter
        num_in_alphabet = alphabet.index(letter)
        # Find the position in the codeword with the letter to shift
        shiftIndex = l % len(codeword)
        # Find the letter in the codeword to shift
        shiftLetter = codeword[shiftIndex]
        # Find the number associated with the letter to be used as the shift
        shift = alphabet.index(shiftLetter)
        # Find the plain_num which is associated with the num_in_alphabet - shift
        # then modulus the length of the alphabet
        plain_num = (num_in_alphabet - shift) % len(alphabet)
        # Find the plain letter by using the new index in the alphabet
        plain_letter = alphabet[plain_num]
        # Add the new letters the blank string
        plaintext = plaintext + plain_letter
        # return the plaintext in all lowercase
    return plaintext.lower()

def breakCaesar(ciphertext):
    for i in range(1,26):
        print(caesar(ciphertext, i ))

def auto(plaintext, codeword):
    for i in range(len(plaintext) - len(codeword)):
        codeword = codeword + plaintext[i]
        print(codeword)
        ciphertext = polyalphabetic(plaintext,codeword)
    return ciphertext


