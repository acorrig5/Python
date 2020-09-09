# This program calculates the balance of a saving account after a period of several years.
# This program asks for: 
#     - initial saving amount
#     - interest rate (as percent)
#     - saving periods (in years)

#Prompt user to enter amount they will deposit to start their account
savingsAmt = float(input('How much are you depositing to the saving account? '))
                   
#Prompt user to enter the number of years they will be keeping their account
years = int(input('How many years are you keeping the account? '))
                      
#Prompt user to enter the interest rate in percent
intRate = float(input('What is the interest rate (%)? '))

#Repetitive Count-Controlled loop to calculate their balance for the number of years provided by user
for yearsSAVED in range(1, (years + 1)):
   #calculate savings balance including interest earned this year
   savingsAmt = savingsAmt + (savingsAmt * float(intRate/100))   
   #display year and new balance with interest earned
   print('After year ', yearsSAVED, ', you have $', format(savingsAmt, ',.2f'), ' in your account', sep='')