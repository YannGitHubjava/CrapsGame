import random


class Dice:

    def __init__(self):
        self.number

    def roll_result(self):
        roll = random.randint(1,6)   # return a random number between 1, and 6 including 6
        return roll                  # Also equal to random.randrange(1, 7)
