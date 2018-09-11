#!/usr/bin/env python3

print('Pay Check Calculator')
print()

#get input from users
hoursWorked = float(input('Hours Worked:\t\t'))
hourlyRate = float(input('Hourly Pay Rate:\t'))

#variable declaration
taxRate = 18

#calculate tax and gross pay
grossPay = hoursWorked*hourlyRate
taxAmount = grossPay*(taxRate/100)
homePay = grossPay - taxAmount

#display results
print()
print('Gross Pay:\t',round(grossPay,2))
print('Tax Rate:\t',round(taxRate,2))
print('Tax Amount:\t',round(taxAmount,2))
print('Take Home Pay:\t',round(homePay,2))
