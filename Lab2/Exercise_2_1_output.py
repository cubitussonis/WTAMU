#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)

# caluculate costs
total_gas_score = round(gallons_used * cost_gallon,1) #total gas cost
cost_mile = round(cost_gallon / mpg,1) #cost per mile

# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t\t" + str(total_gas_score))
print("Cost Per Mile:\t\t\t" + str(cost_mile))
print()
print("GoodBye")
