from main import die


class Player(object):

    def __init__(self, player_name):
        self.name = player_name
        self.player_bet = 0

    # def __str__(self):
    #     return self.name

    # def place_bet(self):
    #     pass

    def roll_die(self):
        input("Press any key to roll the die\n")
        # print(self.name + " is rolling\n")
        combined_roll = 0
        for dice in die:
            number_rolled = dice.roll()
            print(str(number_rolled))
            combined_roll += number_rolled
        return combined_roll
