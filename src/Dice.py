import random
class Dice():
    D1 = random.randint(1,6)
    D2 = random.randint(1,6)
    D3 = random.randint(1,6)
    D4 = random.randint(1,6)
    D5 = random.randint(1,6)

    rolls_allowed = 2

    def announce_dices(self):
        print(f"""Le tirage : \nD1 : {self.D1}\nD2 : {self.D2}\nD3 : {self.D3}\nD4 : {self.D4}\nD5 : {self.D5}""")

    def reroll(self, id_dice):
        setattr(self, id_dice, random.randint(1,6))
    
    def decrease_rolls(self):
        self.rolls_allowed -= 1

    def reroll_authorized(self):
        return self.rolls_allowed > 0

