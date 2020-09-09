# IT 5413 Test 2 Question 1 - Amy Corrigan

# Write a simple dictionary program that allows users to enter an English word then outputs the meaning of the word.
# If the entered word is not in the dictionary then outputs a message.
try:       # exception handling
    #defining the words in our dictionary.
    dictEnglish = {
        'cat': 'a small domesticated carnivore, Felis domestica or F. catus, bred in a number of varieties.',
        'dog': 'a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell.',
        'monkey': 'a small to medium-sized primate that typically has a long tail.',
        'rabbit': 'a burrowing, gregarious, plant-eating mammal with long ears, long hind legs, and a short tail.',
        'fish': 'a limbless cold-blooded vertebrate animal with gills and fins living wholly in water. '
    }
    word = str(input('DICTIONARY - enter a word: '))  #getting word from user
    if word in dictEnglish:                           #checking if that word is in the dictionary
        print('')                                     #printing a line to make the output look nicer
        print('%s : %s' % (word, dictEnglish[word]))  #printing the word and it's definition
    else:
        print('')                                     #printing a line to make the output look nicer
        print('The word you entered is not in the dictionary: %s' % (word))  #msg to user
except ValueError:                   #exception handling
        print('ERROR: invalid word entered, please restart!')