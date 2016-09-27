"""
Dice Game that gets result from rolling two dices and add the result.
The rule to win the Craps game will be established later in development stage

"""

from dice import *


def main():

    while True:
        choice = input("Ready to start playing Craps??")
        if choice.upper() == "YES":
            print("Rolling dice ....")
            roll1 = Dice.roll_result(None)
            roll2 = Dice.roll_result(None)
            print("dice result after rolling is roll1= " + str(roll1) + " and roll2 = " + str(roll2) )

            total_result = roll1 + roll2

            print("Your roll result is: " + str(total_result))

        else:
            print(" **** Good bye ****")
            break

main()
