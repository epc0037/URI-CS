# CSC 110: Spring 2016 (Section 1)
# Week 11: Operating Systems Algorithms (Lab)

############################
#                          #
# Shortest Job First (SJF) #
#      Scheduler           #
#                          #
############################

# Given: A list of processes with execution times
# Find: A schedule of the processes using Shortest Job First (SJF)

import queue

# Function to get the time slice value and the processes from the file into the queue
# Queue will contain a string with process ID and exec time separated by a comma

def getProcs():
    fname = input("Enter the name of the file containing the processes: ")
    inFile = open(fname, 'r')

    procList = []
    execList = []
   
    line = inFile.readline()                                              
    # Loop through the file inserting processes into the list
    while line != '':                             
        line = line.strip()
        PID,execTime = line.split(',')
        procList = procList + [PID]
        execList = execList + [int(execTime)]
        line = inFile.readline()
    inFile.close()
    return procList, execList

# Function to print the contents of the queue
def printQueue(procList, execList):
    for i in range(len(procList)):
        print(str(procList[i]+','+str(execList[i])))
        
# Function to find the shortest process
def findShortestProcess(execList):
    shortest = execList[0]
    for i in range(1, len(execList)):
        if execList[i] < shortest:
            shortest = execList[i]
    shortestPos = execList.index(shortest)
    return shortestPos
    

# Function to execute the processes in the queue

def scheduleSJF(execList, procList):
    for i in range(len(execList)):
        index = findShortestProcess(execList)
        PID = procList.pop(index)            
	# Convert exectime to an integer
        exectime = int(execList.pop(index))                    
        print("Getting next process - Process ", PID," has ", exectime," instructions to execute")
	# Initialize the timer
        timer = 0                                   
	# While proc still has time in slice and still has code to execute
        while (exectime > 0):  
	    # Execute an instruction of process
            exectime = exectime - 1                         
	    # Count one tick of the timer
            timer = timer + 1                       
            print("Executing instruction ", exectime," of process ", PID,".  Timer = ", timer)
        print("*** Process ", PID, " Complete ***")
    return

def main():
    # Get the data from the file
    procList, execList = getProcs()

    # Print the queue
    printQueue(procList, execList)

    # Schedule the processes
    scheduleSJF(execList, procList)
