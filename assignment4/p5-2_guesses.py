#!/usr/bin/env python3

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    # limit must be at least 2, otherwise the game makes no sens
    while limit < 2:
        print("Smallest possible limit is 2. Please enter valid input.")
        limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print("I'm thinking of a number from 1 to " + str(limit) + "(included).\n")
    count = 1 # initializing the counter
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            return

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game(limit) #starting the game with the limit set
        again = input("Play again? (y/n): ")
        #asking again if invalid input
        while again.lower()!="y" and again.lower()!="n":
            print("Invalid entry. Please enter 'y' or 'n'.")
            again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

