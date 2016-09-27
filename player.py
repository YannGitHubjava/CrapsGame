from dice import *
die = (Dice(), Dice())


class Player(object):

    def __init__(self, name):
        self.name = name
        self.player_bet = 0

    # def __str__(self):
    #     return self.name

    def place_bet(self):
        pass

    def roll_die(self):
        input("Press any key to roll the die\n")
        print(self.name.title() + " is rolling\n")
        combined_roll = 0
        for dice in die:
            number_rolled = dice.roll()
            print(str(number_rolled))
            combined_roll += number_rolled
        return combined_roll
