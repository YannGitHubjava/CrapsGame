"""
Dice Game that gets result from rolling two dices and add the result.
The rule to win the Craps game will be established later in development stage

"""
from player import *
import gameplay


def start_game():
    print('Welcome to Craps\n')
    name = input('Please enter your name: \n')
    while True:
        balance = input("Please enter how much money you have: \n")
        if balance == '':
            break
        try:
            balance = float(balance)
            break
        except ValueError:
            print("Please enter a correct value")
            continue

    return Player(name, balance)


def main():

    player1 = start_game()
    while True:
        gameplay.player_turn(player1)

main()
