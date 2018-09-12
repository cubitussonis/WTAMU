#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = int(input("Please enter the length: "))
width = int(input("Please enter the width:  "))

# calculate area
area = length * width

# calculate perimeter
perimeter = (2*length)+(2*width)
            
# format and display the result
print()
print("Area =",area)
print("Perimeter =",perimeter)
print()
print("Thanks for using this program ! Bye")


