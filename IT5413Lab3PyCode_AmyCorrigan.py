## In 2017, the tuition for a full-time student in a university is $6,450 per year.

#setting start year
actualYear = 2017

## The tuition will be going up for the next 7 years at a rate of 3.5% per year.

#setting fixed interest rate
INT_RATE = .035

#setting end year
endYear = 2025

## Write your program using a loop that displays the projected year tuition for the next 7 years.
## You should display the actual year (2018, 2019, through 2024) and the tuition amount per year.
#This is my loop that to begin with the start year and end with my endYear
for year in range(actualYear, endYear):
   if year == 2017:             #this should only execute once on the first iteration
      tuition = 6450.00         #setting start tuition
      print('Tuition for', year, 'is $', format(tuition, ',.2f'))
      tuition = tuition + (tuition * INT_RATE)    #calculating tuition + interest for the next yr
   else:
      print('Tuition for', year, 'is $', format(tuition, ',.2f'))
      tuition = tuition + (tuition * INT_RATE)    #calculating tuition + interest for the next yr