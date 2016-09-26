import random

class dice_Rolling:

    def roll_reuslt(self):
        roll = random.randint(1,6)   # retun a random number between 1, and 6 including 6
        return roll                   #Also equal to random.randrange(1, 7)
