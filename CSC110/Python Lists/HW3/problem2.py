# Evan Carnevale
# CSC 110 - Survey of Computer Science
# Professor Albluwi
# Homework 3 - Problem 2
# This program will prompt the user to enter the
# number of students in a class.
# The program will generate a list of grades in the range of
# 0 to 100. The program will also display the highest grade in the class,
# the lowest grade in the class, and the average of the class grades.
# For each student grade less than or equal to 70, 2 points will be added
# and for each grade more than 70, 1 point will be added.

# create an empty grade list & prompt the user to enter the number of students
# this will set the number of times the program will loop in comparison to i
# which represents the counter.
gradeList = []
number_of_students = int(input("Enter the number of students in the class: "))
i = 0

# here is the while loop which will prompt the user to enter a grade
# for the number of students entered. the counter will increase by 1
# and the program will add a 0 to the list if a number greater than 100 or less than 0
# is entered
while i < number_of_students:
    grade = int(input("Enter the student's grade: "))
    if grade > 100 or grade < 0:
        gradeList = gradeList + [0]
        i = i + 1
    else:
        gradeList = gradeList + [grade]
        i = i + 1
        
# output to the user
print(gradeList)

# here we are setting the highest grade to the first element in the list
# and the lowest grade to the last element in the list.
# each loop will read through the gradeList and assign the appropriate value to
# the highest/lowest grade variables
highest_grade = gradeList[0]
lowest_grade = gradeList[-1]
for k in range(1, len(gradeList)):
    if gradeList[k] > highest_grade:
        highest_grade = gradeList[k]
for i in range(1, len(gradeList)):
    if gradeList[i] < lowest_grade:
        lowest_grade = gradeList[i]

            
# output to the user displaying highest/lowest grades as well as
# the average which is the sum of all the elements in the list divided
# by the length of the list
print("The highest grade in the class is: ", highest_grade)
print("The lowest grade in the class is: ", lowest_grade)
print("The class average is of all the grades is: ", sum(gradeList)/len(gradeList))

# at first, I had this portion directly below my lowest grade lines of code
# but I decided to move it down here because it was affecting the average.
# I reference the same gradeList and for some reason it was using the
# new operations below, calculating the average of the new scores, which I
# did not want it to do. These loops add 2 points to scores less than or equal to
# 70 and add 1 point to grades higher than 70.
for j in range(0, len(gradeList)):
    if gradeList[j] <= 70:
        gradeList[j] += 2
    else:
        gradeList[j] += 1

# final output printing the updated grades with the scale in a new list        
print("The new list of grades: +2 points if (your score) <= 70 or +1 point if \
(your score) > 70: ", gradeList)
