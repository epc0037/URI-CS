# Evan Carnevale
# Professor Albluwi
# CSC 110
# Week 5 Files : Class Activity
# This program will act as a virus on my other python programs!!!

def pythonCrasher(filename):
    inFile = open(filename, 'r')

    data = []

    line = inFile.readline()
    while line != '':
        if line[0] == 'd':
            line = line.capitalize()
        data = data + [line]
        line = inFile.readline()
    inFile.close()

    outFile = open(filename, 'w')
    for i in range(len(data)):
        outFile.write(data[i])
    outFile.close()
