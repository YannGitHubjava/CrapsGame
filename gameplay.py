# TODO define basic functions that test dice rolls according to the Craps rules
# TODO and tells whether the Shooter won or lost a bet
from player import *

def player_turn(player):
    # Puck Off
    # PassLine Bet
    # Shooter Rolls
    while True:
        play_bet = input('Place a bet: \n')
        if play_bet == '':
            break
        try:
            play_bet= float(play_bet)
            break
        except ValueError:
            print("Please enter a correct value")
            continue
    player.setPlayer_bet(play_bet)
    number_rolled = player.roll_die()
    # Come Out Roll
    come_out_roll(number_rolled, player)


def come_out_roll(number_rolled, player):
    # Roll

    if number_rolled == 7 or number_rolled == 11:
        # player wins
        player.set_player_win_bet()
        print("You win \n")
        print("Your new balance " + str(player.get_palyer_balance()) + "\n\n")

    elif number_rolled == 2 or number_rolled == 3 or number_rolled == 12:
        # player loses
        player.set_player_loose_balance()
        print("You lose \n\n")
        print("Your new balance " + str(player.get_palyer_balance()))
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
            player.set_player_loose_balance()
            print("You lose \n\n")
            print("Your new balance " + str(player.get_palyer_balance()))
            return
        elif number_rolled == point:
            # player wins
            player.set_player_win_bet()
            print("You win\n\n")
            print("Your new balance " + str(player.get_palyer_balance()))

            return
        else:
            # Roll Again
            continue
