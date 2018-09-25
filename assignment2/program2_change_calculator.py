#! /usr/bin/env python3

#welcome message
print("Change Calculator")

choice = "y"
while choice.lower() == "y":
    
    # user input until number cents not between 0 and 99
    nCents = int(input("\nEnter number of cents (0-99): "))
    while nCents < 0 or nCents > 99:
        print("Number of cents must be between 0 and 99. Please try again")
        nCents = int(input("Enter number of cents (0-99): "))

    # Calulating process
    # number of coin is: number cents // coin value
    # new number of cents is the reminder: number cents % coin value
    # starting from biggest coin value to lowest
    nQuarters = nCents // 25 # quarters
    nCents = nCents % 25
    nDimes = nCents // 10 # Dimes
    nCents = nCents % 10
    nNickels = nCents // 5 # nickels
    nCents = nCents % 5
    nPennies = nCents // 1 # pennies

    # displaying results
    print("\nQuarters:",nQuarters)
    print("Dimes:   ",nDimes)
    print("Nickels: ",nNickels)
    print("Pennies: ",nPennies)

    # asking to start again
    choice = input("\nContinue? (y/n): ")
    while choice.lower() != "y" and choice.lower() != "n":
        choice = input("Continue? (y/n): ")
        
print("\nBye!")
