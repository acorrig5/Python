#!/usr/bin/env python
# coding: utf-8

# In[52]:


#IT5413 Lab 4 - Amy Corrigan
# This program accepts a Student Name and 8 numeric test scores (out of 100).
# The 8 numeric test scores are averaged and a letter grade is assigned.
# The name of the student and the student's grade is displayed at the end.

### Function Definitions ###
def calc_average():
    "This function accepts a list of 8 numeric test scores and returns the average of the scores"
    testAvg = int(0)
    for i in range(1, 9):
        testScore = int(input('Please enter a test score %d: ' % i))
        while testScore < 0 or testScore > 100:
           print('Invalid Test Score Entered!')
           testScore = int(input('Please enter a valid test score %d: ' % i))
        testAvg += testScore
    testAvg /= i
    int(testAvg)
    return testAvg
    
def determine_grade(num):
    "This function receives the test average and returns the letter grade"
    if num < 60:
        letterGrade = "F"
    elif num <= 69:
        letterGrade = "D"
    elif num < 79:
        letterGrade = "C"
    elif num < 89:
        letterGrade = "B"
    elif num <= 100:
        letterGrade = "A" 
    else:
        print('Letter grade cannot be calculated at this time, please try again.')
    return letterGrade

####   MAIN PROGRAM   ####
studentName = input('Please enter the student name: ')
while studentName == '':     #input validation loop
    print('Incorrect entry!')
    studentName = input('Please enter a valid student name: ')
else:
    try:
        avg = calc_average()
        letter = str(determine_grade(avg))
        print('---')
        print('The letter grade of %s is %s' % (studentName, letter) )
    except ValueError:
        print('ERROR: invalid test score entered, please restart!')

