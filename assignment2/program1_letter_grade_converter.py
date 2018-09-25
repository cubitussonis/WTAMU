#! /usr/bin/env python3

#welcome message
print("Letter Grade Converter")

choice = "y"
while choice.lower() == "y":
    #user input grade assuming he enters valid value
    numGrade = int(input("\nEnter numerical grade: "))

    # ask again if grade less than 0 or above 100
    while numGrade < 0 or numGrade > 100:
        print("Grade must be between 0 and 100. Please try again")
        numGrade = int(input("Enter numerical grade: "))

    letterGrade = "" # initializing letterGrade
    # assigning letterGrade value according to numerical grade
    if numGrade >= 88:
        letterGrade = "A"
    elif numGrade >= 80:
        letterGrade = "B"
    elif numGrade >= 67:
        letterGrade = "C"
    elif numGrade >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"

    # displaying result
    print("Letter grade: "+letterGrade)

    # asking to start again
    choice = input("\nContinue? (y/n): ")
    while choice.lower() != "y" and choice.lower() != "n":
        choice = input("Continue? (y/n): ")

print("\nBye!")
