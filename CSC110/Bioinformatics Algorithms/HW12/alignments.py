# Evan Carnevale
# Professor Albluwi
# CSC 110: Survey of Computer Science - Spring 2016
# Week 12: Bioinformatics Algorithms 
# Homework Assignment

import random

# -----------------------------------------------------------
# ------------------ Do not change this section -------------
# generate random DNA sequence
def randomDNA(length):
    bases = ['A', 'T', 'C', 'G']
    sequence = ""
    for i in range(length):
        sequence = sequence + bases[random.randint(0,3)];
    return sequence

# return two random sequences, the shorter sequence first
def getSequences():
    length1 = int(input('Enter length of sequence 1: '))
    length2 = int(input('Enter length of sequence 2: '))
    
    if length1 < length2:
        sequence1 = randomDNA(length1)
        sequence2 = randomDNA(length2)
    else:
        sequence1 = randomDNA(length2)
        sequence2 = randomDNA(length1)
    return sequence1, sequence2

# print a list of elements, each element in a separte line
def printList(inputList):
    for i in range(len(inputList)):
        print(inputList[i])

# sorts elements in a list using insertion sort algorithm
def insertionSort(inputList):
    for marker in range(1, len(inputList)):
        currentValue = inputList[marker]
        previousIndex = marker - 1
        #slide back the list until you find the smallest
        while previousIndex >=0:
            if currentValue < inputList[previousIndex]:
                # swap
                temp = inputList[previousIndex]
                inputList[previousIndex] = inputList[previousIndex + 1]
                inputList[previousIndex + 1] = temp
                previousIndex = previousIndex - 1
            else:
                break
    return inputList

# given a list remove all elments that are duplicates
# the output will be a list of all distinct elements
def removeDuplicates(inputList):
    return insertionSort(list(set(inputList)))


# insert a gap at position "pos" in a given sequence
def insertGap(sequence, pos):
    if pos > len(sequence) or pos < 0:
        return 'Error: Invalid position'
    return sequence[0:pos]+'-'+sequence[pos:len(sequence)]  
# -----------------------------------------------------------
# ---------------- Put your Solutions Here ------------------
    
# Problem 1
# generate all possible variation of a given sequence
# after inserting one gap
# example: generateOneGapAlignment('AB') -->
# ['-AB', 'A-B', 'AB-']
def generateOneGapAlignments(sequence):
    # Create an empty list
    alignments = []
    # Loop through sequence, produces an error if the sequence is empty
    if sequence == '':
        return 'Error: invalid input'
    # Loop through sequence when it is not empty,
    else:
        # i represents an integer in sequence, which increments in the for loop
        for i in range(len(sequence)):
            # Call the insertGap() function and appends that string to the alignments list
            alignments.append(insertGap(sequence, i))
            # Appends the final value for i to the alignments list
        alignments.append(insertGap(sequence, i+1))
        # Output - return the alignments list
        return alignments
    


# Problem 2
# insert gaps into the start of seq1 until it is of equal length to seq2
def align(seq1, seq2):
    # Create a new variable which stores the first gap in the new sequence
    new_seq="-"
    # Conditonal statement that returns an error if the first sequence is empty
    if seq1 == '':
        # Output - return an error
        return 'Error: Invalid input: seq1 is empty'
    # Conditional statement that returns an error if the second sequence is shorter than the first sequence
    elif len(seq2) < len(seq1):
        # Output - return an error
        return 'Error: Invalid input: seq2 is shorter than seq1'
    # Conditional statement that returns the first sequence if both sequence lengths are equal
    elif len(seq1) == len(seq2):
        # Output - return the first sequence
        return seq1
    # Final conditional statement for all other cases
    else:
        # loop that iterates until the sequence lengths are equal
        while len(seq1) != len(seq2):
            # finds the difference between the second and first sequences
            DIFF = len(seq2) - len(seq1)
            # Loop through the difference - 1 to get the positions where the gaps need to be placed
            for i in range(DIFF-1):
                # Adds a '-' for every position in the range of difference - 1
                new_seq = new_seq+"-"
                # Concatenates the first sequence to the gaps to make the length of first sequence to equal the length of the second sequence
            new_seq = new_seq + seq1
            # Output - return the new sequence
            return new_seq
    

# Problem 3
# score an alignment of two sequences
# 1-If there is a gap and a character, score = -1
# 2-If the two characters are different, score = 0
# 3-If the two characters are equal to ‘A’ or ‘G’, score = 1
# 4-If the two characters are equal to ‘C’ or ‘T’, score = 2
def score(seq1, seq2):
    # Initialize the score to 0
    score = 0
    # Tests the lengths of the sequences, if they are not equal, produce an error
    if len(seq1) != len(seq2):
        # Output - returns an error
        return 'Error: the two sequences are not aligned'
    # Conditional for remaining cases
    else:
        # i represents an integer in the first sequence, which is incremented by the loop
        for i in range(len(seq1)):
            # Subtracts 1 from the score if there is a gap in the sequences
            if seq1[i] == '-' or seq2[i] == '-':
                score = score - 1
            # Nothing is added if the characters are different
            elif seq1[i] != seq2[i]:
                score = score
            # Adds 1 to the score if the characters in the sequences match and also equal 'A' or 'G'
            elif seq1[i] == seq2[i] and seq1[i] == 'A' or seq1[i] == 'G':
                score = score + 1
            # Adds 2 two the score if the characters in the sequences match and also equal 'C' or 'T'
            elif seq1[i] == seq2[i] and seq1[i] == 'C' or seq1[i] == 'T':
                score = score + 2
        # Output - returns the score of matches between the two sequences
        return score


# Problem 4  
# given a sequence, generate all possible insertions of two gaps into that sequence
def generateTwoGapAlignments(sequence):
    # Create an empty list
    seq_list = []
    # Loop through sequence, produces an error if the sequence is empty
    if sequence == '':
        return 'Error: invalid input'
    # Loop through sequence when it is not empty,
    else:
        # Definitely had issues here with the code. Although my output
        # exactly matches the provided sample output, there must be an easier way to do what I am trying
        # to accomplish instead of repeating these statements for these new sequences. Each time a character is added,
        # I had to basically create a new sequence and input a gap after each letter. My first few times debugging
        # I noticed I was missing the middle cases (ex. 'A--B', 'AB--C' and so on). This method works but
        # is very tedious (code is already looking very, very long). My guess as to how to fix my program
        # would be to loop through the sequence first, inputing the first dash each time at different
        # positions, then nest another loop calling the insertGap() function. TA Natalie helped me a lot in the
        # first 2 problems, which I was definitely overthinking all weekend. She recommended print statements
        # to track variables that increment and see exactly what my values were at certain points during the loop and to comment
        # before each statement so I could also see just what I was trying to accomplish with that given statement.
        new_seq1 = '-' + sequence
        new_seq2 = sequence + '-'
        new_seq3 = sequence[:1]+ '-' + sequence[1:len(sequence)]
        new_seq4 = sequence[:2] + '-' + sequence[2:len(sequence)]
        new_seq5 = sequence[:3] + '-' + sequence[3:len(sequence)]
        new_seq6 = sequence[:4] + '-' + sequence[4:len(sequence)]
        # i represents an integer in sequence, which increments in the for loop
        for i in range(len(sequence)+1):
            # Call the insertGap() function and appends that string with inserted gaps to the alignments list
            seq_list.append(insertGap(new_seq1, i))
            seq_list.append(insertGap(new_seq2, i))
            seq_list.append(insertGap(new_seq3, i))
            seq_list.append(insertGap(new_seq4, i))
            seq_list.append(insertGap(new_seq5, i))
            seq_list.append(insertGap(new_seq6, i))
        seq_list.append(insertGap(new_seq1, i+1))
        seq_list.append(insertGap(new_seq2, i+1))
        seq_list.append(insertGap(new_seq3, i+1))
        seq_list.append(insertGap(new_seq4, i+1))
        seq_list.append(insertGap(new_seq5, i+1))
        seq_list.append(insertGap(new_seq6, i+1))
        # Calls the removeDuplicates() function to remove and repeating sequences in the list
        alignments = removeDuplicates(seq_list)
        # Output - return the alignments list
        return alignments

# Problem 5
# given a sequence and two alignments - check which alignments give a better score
def compareAlignments(alignment1, alignment2, sequence):
    # returns an error if the lengths of each sequence and alignment are not equal
    if len(alignment1) != len(sequence) or len(alignment2) != len(sequence):
        return 'Error: alignment-sequence length mismatch'
    else:
        # Call to the score() function which returns each score for each comparison we make
        score1 = score(alignment1, sequence)
        score2 = score(alignment2, sequence)
        # If statements that depend on each returned score
        if score1 > score2:
            # Output - return the score of alignment1
            return 'Alignment1 ' + alignment1 + ' has a better alignment score = ' + str(score1)
        elif score2 > score1:
            # Output - return the score of alignment2
            return 'Alignment2 ' + alignment2 + ' has a better alignment score = ' + str(score2)
        else:
            # Output - return the equal scores of alignment1 and alignment2
            return 'Alignment1 ' + alignment1 + ' and Alignment2 ' + alignment2 + ' have an equal score = ' + str(score1)
    
        

