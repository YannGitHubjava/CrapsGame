# TODO define basic functions that test dice rolls according to the Craps rules
# TODO and tells whether the Shooter won or lost a bet
from player import *


def player_turn(player):
    # Puck Off
    # PassLine Bet
    # Shooter Rolls
    number_rolled = Player(player.roll_die())
    # Come Out Roll
    come_out_roll(number_rolled)


def come_out_roll(number_rolled):
    # Roll
    if number_rolled == 7 or number_rolled == 11:
        # player wins
        print("You win")
    elif number_rolled == 2 or number_rolled == 3 or number_rolled == 12:
        # player loses
        print("You lose")
    else:
        # player goes to point round
        point_round(number_rolled)


def point_round(number_rolled):
    # Marker On
    point = number_rolled
    while True:
        # Roll
        if point == 7:
            # player loses, and the next player gets the die
            print("Seven Out")
            return
        elif point == number_rolled:
            # player wins
            print("You win")
            return
        else:
            # Roll Again
            continue
