import random
class Dice():
    D1 = random.randint(1,6)
    D2 = random.randint(1,6)
    D3 = random.randint(1,6)
    D4 = random.randint(1,6)
    D5 = random.randint(1,6)

    def reroll(self, id_dice):
        setattr(self, id_dice, random.randint(1,6))

