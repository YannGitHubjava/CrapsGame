from random import choice


class Dice:

    def __init__(self, sides=6):
        self.sides = range(1, sides+1)

    def roll(self):
        # return a random number between 1, and 6 inclusive
        return choice(self.sides)
