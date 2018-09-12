#!/usr/bin/env python3
        
def get_float(message, lowValue, highValue):
    while True:
        try:
            fNumber = float(input(message))
            while fNumber <= lowValue or fNumber > highValue :
                print("Entry must be greater than",lowValue,
                      "and less than or equal to",highValue)
                fNumber = float(input(message))
            break
        except ValueError:
            print("Error, please enter a number")
            continue
    return fNumber

def get_int(message, lowValue, highValue):
    while True:
        try:
            nNumber = int(input(message))
            while nNumber <= lowValue or nNumber > highValue :
                print("Entry must be greater than",lowValue,
                      "and less than or equal to",highValue)
                nNumber = int(input(message))
            break
        except ValueError:
            print("Error, please enter a number")
            continue
    return nNumber

def main():
    choice = "y"
    while choice.lower() == "y":
        testFloat = get_float("Enter a float: ",0,100)
        testInt = get_int("Enter an int: ",0,100)
        
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
