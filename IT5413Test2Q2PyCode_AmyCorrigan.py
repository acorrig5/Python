#!/usr/bin/env python
# coding: utf-8

# In[39]:


# IT 5413 Test 2 Question 2 - Amy Corrigan

# This program allows a user to enter a sentence, a word they want to replace in that sentence,
# and the word that is replacing the previous word.
# Output is a new sentence with the words switched out.

# MAIN PROGRAM #
try:
    # Prompt user for the sentence and words being found and replaced with
    sentence = input('Please enter a sentence: ')
    findWord = input('Please enter the word to replace: ')
    replaceWord = input('Please enter the replacement word: ')
    
    listSentence = []                      #creating a new list
    listSentence = sentence.split(' ')     # slitting the input into list entries
    
    while findWord in listSentence:        #while loop while the word is still found in the sentence
        foundIndx = listSentence.index(findWord)    # getting index location of the word found
        listSentence[foundIndx] = replaceWord       # updating list with the replacement word
    else:
        newSentence = ''                            #when finished - creating new sentence
        for i in range(len(listSentence)):          # for loop to reconstruct the new sentence
            newSentence += listSentence[i] + ' '    # adding the words with spaces
        print(' ')                                  # printing the final sentence.
        print('Your new sentence is: ')
        print(newSentence)
    
except ValueError:
    print('That word was not found in the sentence.')

