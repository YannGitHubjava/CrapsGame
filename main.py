"""
Dice Game that gets result from rolling two dices and add the result.
The rule to win the Craps game will be established later in development stage

"""
from player import *
from dice import *

die = (Dice(), Dice())


def start_game():
    print("Welcome to Craps\nPlease enter your name")
    player = input("> ")


def main():

    while True:
        user = input("Ready to start playing Craps??")
        if user.upper() == "YES":
            print("Rolling dice ....")
            combined_roll = 0
            for dice in die:
                number_rolled = dice.roll()
                print(str(number_rolled))
                combined_roll += number_rolled

            print("Your roll result is: " + str(combined_roll))

        else:
            print(" **** Good bye ****")
            break

main()
