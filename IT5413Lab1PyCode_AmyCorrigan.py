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

# Ask the guest for the gratuity percent
GratuityPercent = float(input('Gratuity Percent: '))

# Calculate gratuity using the item sum and gratuity percent
Subtotal = Appetizer + Entree + Drink + Dessert
Total = Subtotal + (Subtotal * float(GratuityPercent/100))

#Output the total amount the guest will be paying
print('------')
print('You will have to pay $', format(Total, ',.2f'), sep='')