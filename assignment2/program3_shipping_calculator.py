#! /usr/bin/env python3

#welcome message
print("==================================================")
print("Change Calculator")

choice = "y"
while choice.lower() == "y":
    print("==================================================")
    # user input must be > 0
    # rounding it, 2 digits after coma, cause it's a price
    itemsCost = round(float(input("Cost of items ordered:\t")),2)
    while itemsCost < 0:
        print("You must enter a positive number. Please try again")
        itemsCost = round(float(input("Cost of items ordered:\t")),2)

    # assigning good shipping cost
    shippingCost = 0
    if itemsCost < 30:
        shippingCost = 5.95
    elif itemsCost < 50:
        shippingCost = 7.95
    elif itemsCost < 75:
        shippingCost = 9.95
    else:
        shippingCost = 0

    # calculating total cost
    totalCost = round(itemsCost+shippingCost,2)

    # changing shipping cost to display 'FREE' instead of 0
    if shippingCost == 0:
        shippingCost = "FREE"

    # displaying result
    print("Shipping cost:\t\t"+str(shippingCost))
    print("TotalCost:\t\t"+str(totalCost))
    
    # asking to start again
    choice = input("\nContinue? (y/n): ")
    while choice.lower() != "y" and choice.lower() != "n":
        choice = input("Continue? (y/n): ")

print("==================================================")
print("Bye!")
