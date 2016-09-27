# TODO define basic functions that test dice rolls according to the Craps rules
# TODO and tells whether the Shooter won or lost a bet
from player import *


def player_turn(player):
    # Puck Off
    # PassLine Bet
    # Shooter Rolls
    number_rolled = player.roll_die()
    # Come Out Roll
    come_out_roll(number_rolled, player)


def come_out_roll(number_rolled, player):
    # Roll
    if number_rolled == 7 or number_rolled == 11:
        # player wins
        print("You win")
    elif number_rolled == 2 or number_rolled == 3 or number_rolled == 12:
        # player loses
        print("You lose")
    else:
        # player goes to point round
        point_round(number_rolled, player)


def point_round(number_rolled, player):
    # Marker On
    point = number_rolled
    print("The point is " + str(number_rolled))
    while True:
        # Roll
        number_rolled = player.roll_die()
        if number_rolled == 7:
            # player loses, and the next player gets the die
            print("Seven Out")
            return
        elif number_rolled == point:
            # player wins
            print("You win")
            return
        else:
            # Roll Again
            continue
