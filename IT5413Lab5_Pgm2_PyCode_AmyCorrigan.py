#!/usr/bin/env python
# coding: utf-8

# In[48]:


#IT5413 Lab 5 Program 2 - Amy Corrigan
# This program reads from golf.txt
# the player's first and last name, handicap, and golf score
# and displays the data on the screen.

### Function Definitions ###

####   MAIN PROGRAM   ####
#open golf.txt to read
golf_txt = open(r'c:\python\golf.txt', 'r') 
try:
    print('Marietta Country Club Tournament Players, Handicaps, and Scores: ')
    print("Player # | First & Last Name | Handicap | Score")
    print(' ')
    num_players = 16
    for i in range(1, num_players):
        playerRecd = golf_txt.readline()
        playerRecd = playerRecd.rstrip('\n')
        pr = playerRecd.split()  
        fname, lname, hcap, scr = pr[0], pr[1], pr[2], pr[3] #parsing out the pieces of the golfer record
        hcap = float(hcap)
        scr = int(scr)
        print("Player %d:    %s %s       %.2f         %d" % (i, fname, lname, hcap, scr))
    golf_txt.close()
    print(' ')
    print('Congratulations to all of the golfers and thank you for participating!')
except ValueError:
    print('ERROR: invalid entry, please restart!')

