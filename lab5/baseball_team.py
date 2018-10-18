#!/usr/bin/env python3

def main():
    print("\t\t Basebal Team Manager")
    print("This program calculates the batting average for a player based on the player's oficial number of at bats and hits")
    print()
    menu()

    option = int(input('Menu option: '))

    #verify correct option
    while(option != 1 and option != 2):
        print('Not a valid option! Please try again')
        print()
        menu()
        option = int(input('Menu option: '))

    while(option == 1):
        # get input from the user
        print()
        playerName= str(input("Player's name: "))
        numberBats= int(input("Official number of at bats: "))
        numberHits= int(input("Number of hits: "))
        average = calculBattingAverage(numberHits,numberBats)
        
        while(numberBats<numberHits or numberBats <0 or numberHits<0):
            print("incorrect data")
            numberBats= int(input("Official number of at bats: "))
            numberHits= int(input("Number of hits: "))
        # format and display the result
        print()
        print(playerName+"'s batting average is "+str(average))
        print()
        print()
        menu()
        option = int(input('Menu option: '))

        #verify correct option
        while(option != 1 and option != 2):
            print('Not a valid option! Please try again')
            print()
            menu()
            option = int(input('Menu option: '))
    print('Bye');

def menu():
    print('MENU OPTIONS')
    print('1 - Calculate batting average')
    print('2 - Exit program')



# calculate the average
def calculBattingAverage(numberHits,numberBats):
    return float(round(numberHits/numberBats, 3))

if __name__=="__main__":
    main()



