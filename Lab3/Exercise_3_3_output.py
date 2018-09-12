#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":
    # initializing variables
    monthly_investment = 0
    yearly_interest_rate = 0
    years = 0
    # get input from the user
    
    while monthly_investment <= 0:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment <= 0:
            print("Entry must be greater than 0. Please try again")
    while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate <= 0 or yearly_interest_rate > 15:
            print("Entry must be greater than 0 and less or equal to 15.\n"
                  +"Please try again")
    while years <= 0 or years > 50:
        years = int(input("Enter number of years:\t\t"))
        if years <= 0 or years > 50:
            print("Entry must be greater than 0 and less or equal to 50.\n"
                  +"Please try again")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months): # from 0 to #months so real month is i+1
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        # display the result
        if (i+1)%12==0:
            print("Year =",int((i+1)/12),"Future Value =",round(future_value, 2))

    print()
    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    while choice!="y" and choice!="n":
        choice = input("Continue (y/n)? ")
    print()

print("Bye!")
