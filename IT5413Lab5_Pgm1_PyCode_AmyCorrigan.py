#!/usr/bin/env python
# coding: utf-8

# In[25]:


#IT5413 Lab 5 Program 1 - Amy Corrigan
# This program accepts player's first and last name, 
# handicap, and golf score as a player record and 
# saves it in a file.
# The output of this program is a file:  golf.txt

### Function Definitions ###

####   MAIN PROGRAM   ####
#open golf.txt to write to
golf_txt = open(r'c:\python\golf.txt', 'w+') 
try:
    num_players = int(input("Please enter number of golfer's in tournament: "))
    if (num_players == 16):
        for i in range(num_players):
            playerFName = input("Please enter the golfer's First Name: ")
            playerLName = input("Please enter the golfer's Last Name: ")
            playerHCap = input("Please enter the golfer's handicap: ")
            playerScore = input("Please enter the golfer's score: ")
            golf_txt.write(playerFName + ' ') 
            golf_txt.write(playerLName + ' ') 
            golf_txt.write(playerHCap + ' ')
            golf_txt.write(playerScore + '\n')
        golf_txt.close()
        print('The Marietta Country Club Golf Tournament player records have been saved to golf.txt')
    else:
        print("Not enough players! Tournament rules require 16 players")
except ValueError:
    print('ERROR: invalid entry, please restart!')

