# Prompt guest and inform them of what data we want them to input
print('Please enter the price for each item')

# Ask the guest for the price of their appetizer
Appetizer = float(input('Appetizer: '))

# Ask the guest for the price of their entree
Entree = float(input('Entree: '))

# Ask the guest for the price of their drink
Drink = float(input('Drink: '))

# Ask the guest for the price of their dessert
Dessert = float(input('Dessert: '))

# Ask the guest for the number of people in their party
Ppl_In_Party = int(input('People in Party: '))

# If there are 5 or more in party then gratuity is 18 percent
# If there are less than 5 in party then Ask for gratuity percent they will pay
if Ppl_In_Party < 5:
# Ask the guest for the gratuity percent
  GratuityPercent = float(input('Gratuity Percent: '))
else:
# Set gratuity percent to 18
  GratuityPercent = 18.0

# Calculate gratuity using the item sum and gratuity percent
Subtotal = Appetizer + Entree + Drink + Dessert
Total = Subtotal + (Subtotal * float(GratuityPercent/100))

#Output the total amount the guest will be paying
print('----')
print('You will have to pay $', format(Total, ',.2f'), sep='')