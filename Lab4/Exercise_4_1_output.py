#!/usr/bin/env python3

import validation

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

##def get_float(message, lowValue, highValue):
##    while True:
##        try:
##            fNumber = float(input(message))
##            while fNumber <= lowValue or fNumber > highValue :
##                print("Entry must be greater than",lowValue,
##                      "and less than or equal to",highValue)
##                fNumber = float(input(message))
##            break
##        except ValueError:
##            print("Error, please enter a number")
##            continue
##    return fNumber
##
##def get_int(message, lowValue, highValue):
##    while True:
##        try:
##            nNumber = int(input(message))
##            while nNumber <= lowValue or nNumber > highValue :
##                print("Entry must be greater than",lowValue,
##                      "and less than or equal to",highValue)
##                nNumber = int(input(message))
##            break
##        except ValueError:
##            print("Error, please enter a number")
##            continue
##    return nNumber

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = validation.get_float("Enter monthly investment:\t",0,1000)
        yearly_interest_rate = validation.get_float("Enter yearly interest rate:\t",0,15)
        years = validation.get_int("Enter number of years:\t\t",0,50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
