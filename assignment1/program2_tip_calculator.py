#!/usr/bin/env python3

print('Tip Calculator')
print()

#get input from users
costMeal = float(input('Cost of meal:\t'))
tipPercent = float(input('Tip percent:\t'))

#calculate tip amount and total amount
tipAmount = (tipPercent/100)*costMeal
totalAmount = costMeal + tipAmount


#display results
print()
print('Tip amount:\t',round(tipAmount,2))
print('Total amount:\t',round(totalAmount,2)) 
