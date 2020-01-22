# Evan Carnevale & Hunter Bastan
# Professor Albluwi
# CSC 110: Survey of Computer Science
# Lab 12: Bioinformatics
# April 15th, 2016

# Function will compute the percentage of matches found between a pair
# of given sequences
def matchPct(seq1, seq2):
    total = 0
    if len(seq1) == 0 and len(seq2) == 0:
        return "Error: both sequences are empty strings"
    elif len(seq2)==0 or len(seq1) == 0:
        return 0.0
    else:
        for i in range(len(seq1)):
            if seq2[i] == seq1[i]:
                total = total + 1
            else:
                total = total
        pct = total / len(seq2)
    return pct

# Function that takes a sequence as input and returns a window
# that starts at 'start' and extends for 'size' elements.
def getWindow(seq, size, start):
    if len(seq) == 0:
        return('Error: sequence is empty')
    elif size <= 0 or size> len(seq):
        return('Error: illegal size')
    elif start < 0 or start >= len(seq):
        return ("Error: illegal start value")
    elif (start + size)> len(seq):
        return("Error extends beyond the sequence length")
    else: 
        return seq[start:start+size]

# Function takes two sequences and returns the percentage
# match of the two given windows
def windowMatchPct(seq1, size1, start1, seq2, size2, start2):
    window1 = getWindow(seq1, size1, start1)
    window2 = getWindow(seq2, size2, start2)
    pct = matchPct(window1, window2)
    return window1, window2, pct

# Function generates a list of stars and/or dashes. A star is generated if the match %
# for a specific window is greater thsn or equal to the threshold.
def slideWindow(seq1, seq2, window, threshold):
    if len(seq1) == 0 or len(seq2) == 0:
        return "Error: one of the sequences is an empty string"
    elif seq1 > seq2:
        return 'Sequence 1 cannot be longer than Sequence 2'
    elif threshold < 0 or threshold > 1:
        return 'Error: invalid threshold value'
    elif window > len(seq1) or window < 1:
        return 'Error: invalid window size'
    myList = []
    window1 = ''
    window2 = ''
    for i in range(window):
        window2 = window2 + seq2[i]
    start = 0
    while start <= (len(seq1) - window):
        for i in range(window):
            window1 = window1 + seq1[i + start]
        start = start + 1
        pct2 = matchPct(window1,window2)
        print('window 1 = ',window1)
        print('Window 2 = ',window2)
        print(pct2)
        window1 = ''
        if threshold > pct2:
            myList = myList + ['-']
        elif threshold <= pct2:
            myList += ['*'] 
    print(myList)
    
def slideAnyWindow(seq1, seq2, window, threshold, direction):
    if direction == 1:
        slideWindow(seq1,seq2,window,threshold)
    elif direction == 2:
        slideWindow(seq2,seq1,window,threshold)
    else:
        return 'Error: invalid direction'
