#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()


choice = "y"
while choice.lower() == "y":
    # get input from the user
    miles_driven= float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t"))
    cost_gallon = float(input("Enter cost per gallon:\t\t"))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_gallon <= 0:
        print("Cost used must be greater than zero. Please try again.")
    else:
        # calculate miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        # caluculate costs
        tgc = round(gallons_used * cost_gallon,1) #total gas cost
        cpm = round(cost_gallon / mpg,1) #cost per mile
        # displaying the results
        print()
        print("Miles Per Gallon:\t\t" + str(mpg))
        print("Total Gas Cost:\t\t\t" + str(tgc))
        print("Cost Per Mile:\t\t\t" + str(cpm))
        
    choice = input("\nGet entries for another trip (y/n)? ")
    while choice!="y" and choice!="n":
        print("Your anwser is incorrect")
        choice = input("Get entries for another trip (y/n)? ")
    print()

print("Bye")
