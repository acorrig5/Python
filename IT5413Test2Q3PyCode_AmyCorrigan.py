#!/usr/bin/env python
# coding: utf-8

# In[71]:


# IT 5413 Test 2 Question 3 - Amy Corrigan

# This program creates a City class that has two attributes - name & population
# The class should be encapsulated with a __str__() method defined.
try:    #exception handling
    class City:                    # City class creation and definition of it's methods

        def __init__(self):            #initialization of it's attributes
            self.__name = ''
            self.__population = ''
        
        def get_name(self):           # get_name method
            return self.__name
    
        def get_population(self):     # get_population method
            return self.__population
    
        def set_name(self, name):     # set_name method
            self.__name = name
    
        def set_population(self, population):  # set_population method
            self.__population = population

        def __str__(self):                   # concatenates and returns a string to print
            return 'The population of ' + self.__name + ' is ' + self.__population + '.'
    
    #setting first city
    firstCity = City()
    firstCity.set_name('Atlanta')
    firstCity.set_population('486290')
    
    #setting second city
    secondCity = City()
    secondCity.set_name('Kennesaw')
    secondCity.set_population('34344')
    
    #setting third city
    thirdCity = City()
    thirdCity.set_name('Marietta')
    thirdCity.set_population('61048')
    
    #setting fourth city
    fourthCity = City()
    fourthCity.set_name('Roswell')
    fourthCity.set_population('91168')
    
    #getting hidden attribute data to the main program
    firstCity.get_name()
    firstCity.get_population()
    secondCity.get_name()
    secondCity.get_population()
    thirdCity.get_name()
    thirdCity.get_population()
    fourthCity.get_name()
    fourthCity.get_population()
    
    #printing city information
    print(firstCity.__str__())
    print(secondCity.__str__())
    print(thirdCity.__str__())
    print(fourthCity.__str__())

except ValueError:                   #exception handling
        print('ERROR, please restart!')

