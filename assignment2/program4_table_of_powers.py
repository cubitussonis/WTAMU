#! /usr/bin/env python3

#welcome message
print("Table of Powers")

choice = "y"
while choice.lower() == "y":

    #user input - start number must be lower than stop number
    startNumber = int(input("\nStart number:\t"))
    stopNumber = int(input("Stop number:\t"))
    while startNumber >= stopNumber:
        print("Error: Start number must be less than stop number. Please try again") 
        startNumber = int(input("Start number:\t"))
        stopNumber = int(input("Stop number:\t"))
        
    #displaying the results
    print()
    print("Number\t|\tSquared\t\t|\tCubed")
    print("======\t|\t=======\t\t|\t=====")
    for i in range(startNumber,stopNumber+1):
        print(str(i)+"\t|\t"+str(i**2)+"\t\t|\t"+str(i**3))
        print("-----------------------------------------------------")

    # asking to start again
    choice = input("\nContinue? (y/n): ")
    while choice.lower() != "y" and choice.lower() != "n":
        choice = input("Continue? (y/n): ")

print("\nBye!")
