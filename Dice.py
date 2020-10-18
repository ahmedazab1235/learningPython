from random import randint

class Dice :
    """dice """
    def __init__(self, sides=6):
        """initilization """
        self.sides = sides
    def roll_die(self):
        """rool a die"""
        print(randint(1, self.sides))

die_1 = Dice(20)
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()