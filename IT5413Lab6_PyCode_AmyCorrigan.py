#!/usr/bin/env python
# coding: utf-8

# In[1]:


##### IT5413 Lab 6 - Amy Corrigan
# This program accepts monthly rainfall data from user as a list.
# This program calculates and displays the total rainfall for the year,
# the average monthly rainfall, and the months with the highest and lowest rainfall.

### Function Definitions ###

####   MAIN PROGRAM   ####
try:                # Exception Handling block
    state = input('What state are you in? ')              # accepting the state in which data was gathered
    # setting the list of months in a year for simplicity
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    annual_rainfall = []           # creating list for the rainfall entries
    m = 0                          # setting our month iterator to pull out the correct month
    total_rainfall = 0             # creating the variable for the total rainfall amount
    for i in [month_list]:         # for loop to parse through the months and gather the rainfall amounts
        while m < 12:              # while loop to ensure we're stopping at the end - maybe I did this wrong??
           monthly_rainfall = float(input("Please enter %s's rainfall (in inches): " % (i[m])))     # getting rainfall amts
           total_rainfall += monthly_rainfall                        # adding up the total rainfall
           annual_rainfall.append(monthly_rainfall)                  # appending the input to the list
           m += 1                                                    # increasing our interator
    avg_rainfall = (total_rainfall/m)      # getting the average rainfall
    print(' ')                             # displaying all the data for the user
    print('RAINFALL STATISTICS FOR:  %s' % (state))
    print('----------------------------------------')
    print('Total annual rainfall:  %.1f' % (total_rainfall))
    print(' ')
    print('Average monthly rainfall:  %.1f' % (avg_rainfall))
    print(' ')
    print('Maximum rainfall in a month:  %.1f' % (max(annual_rainfall)))
    print(' ')
    print('Minimum rainfall in a month:  %.1f' % (min(annual_rainfall)))
except ValueError:
    print('ERROR: invalid entry, please restart!')

