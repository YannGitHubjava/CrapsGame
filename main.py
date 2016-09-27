"""
Dice Game that gets result from rolling two dices and add the result.
The rule to win the Craps game will be established later in development stage

"""

from dice import *
from winBet import *



def main():


    while True:
        choice = input("Ready to start playing Craps??")
        if choice.upper() == "YES":
            print("Rolling dice ....")
            roll1 = dice_Rolling.roll_reuslt(None)
            roll2 = dice_Rolling.roll_reuslt(None)
            print("dice result after rolling is roll1= " + str(roll1) + " and roll2 = " + str(roll2) )

            total_Result = roll1 + roll2

            print("Your roll reulst is: " + str(total_Result))

            """Checking if the result is a win or a lose"""

            game_info = Winning_Check.winning(total_Result)
            print(game_info)

        else:
            print(" **** Good bye ****")
            break

main()