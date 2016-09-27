
#TODO define basic functions that test dice rolls according to the Craps rules
#TODO and tells whether the Shooter won or lost a bet

class Winning_Check:
    @staticmethod
    def winning(result):

        if result == 7 or result == 11:
            return "***print you won**"

        elif result == 2 or result == 3 or result == 12:
             return "***You Crapped out****"

        else:
            return "***Try again***"




