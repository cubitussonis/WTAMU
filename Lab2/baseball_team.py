#!/usr/bin/env python3
print("\t\t Basebal Team Manager")
print("This program calculates the batting average for a player based on the player's oficial number of at bats and hits")
print()

# get input from the user
playerName= str(input("Player's name: "))
numberBats= int(input("Official number of at bats: "))
numberHits= int(input("Number of hits: "))


# calculate the average
average = float(round(numberHits/numberBats, 3))

# format and display the result
print()
print(playerName+"'s batting average is "+str(average))
