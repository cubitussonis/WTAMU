#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
choice = "y"
while choice.lower() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

    # initializing variables
    counter = 0
    score_total = 0
    test_score = 0

    while test_score != "end":
        try:
            test_score = input("Enter test score: ")
            if test_score == "end":
                break
            test_score = int(test_score)
        except ValueError:
            print("Please enter a score between 0 and 100")
            continue
        else:
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")

    # one score must be entered to display a result
    if counter != 0:
        # calculate average score
        average_score = round(score_total / counter)
                        
        # format and display the result
        print("======================")
        print("Total Score:", score_total,
              "\nAverage Score:", average_score)
    else:
        print("======================")
        print("Program ended without entering a test score.")

    choice = input("\nEnter another set of test scores (y/n)? ")
    while choice!="y" and choice !="n":
        choice = input("Enter another set of test scores (y/n)? ")
    print()
print("Bye")


