#! usr/bin/env python3

def evenOddCheck(number):
    """
    Argument: number
    Return: string odd or even
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
#End of EvenOddCheck()

def main():
    print("Even or Odd Checker\n")
    choice = "y"
    while choice.lower() == "y":
        #User input, call even/odd checker and displaying the result
        userNumber = int(input("Enter an integer: "))
        numberType = evenOddCheck(userNumber)
        print("This is an "+numberType+" number.")
        
        #Asking the user to use the program again
        choice = input("Continue? (y/n): ")
        while choice.lower()!="y" and choice.lower!="n":
            choice = input("Wrong input. Continue? (y/n): ")
#End of main()

if __name__ == "__main__":
    main()
