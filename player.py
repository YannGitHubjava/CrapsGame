from dice import *
die = (Dice(), Dice())


class Player(object):

    def __init__(self, name, player_balance=None):
        self.name = name
        self.player_balance = player_balance
        self.bet = 0

    def setPlayer_bet(self, bet):
        self.bet = bet


    def set_player_loose_balance(self):

        try:
            self.player_balance -= self.bet
        except TypeError:
            print("\n***No Cash***\n")
            self.player_balance = 0



    def set_player_win_bet(self):

        try:
            self.player_balance += self.bet
            if self.get_palyer_balance == '' or self.bet == '':
                print("\n***No Cash***\n")
                self.player_balance = 0
            else:
                pass
        except TypeError:
            print("\n***No Cash***\n")
            self.player_balance = 0




    def get_palyer_balance(self):
        return self.player_balance

    def roll_die(self):
        input("Press any key to roll the die\n")
        print(self.name.title() + " is rolling\n")
        combined_roll = 0
        for dice in die:
            number_rolled = dice.roll()
            print(str(number_rolled))
            combined_roll += number_rolled
        return combined_roll
