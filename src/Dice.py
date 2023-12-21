import random
from collections import Counter

class Dice():
    D1 = random.randint(1,6)
    D2 = random.randint(1,6)
    D3 = random.randint(1,6)
    D4 = random.randint(1,6)
    D5 = random.randint(1,6)

    dice_set = [D1,D2,D3,D4,D5]

    rolls_allowed = 2

    def announce_dices(self):
        print(f"""Le tirage : \nD1 : {self.D1}\nD2 : {self.D2}\nD3 : {self.D3}\nD4 : {self.D4}\nD5 : {self.D5}""")

    def reroll(self, id_dice):
        setattr(self, id_dice, random.randint(1,6))
        self.dice_set = [self.D1, self.D2, self.D3, self.D4, self.D5]
    
    def decrease_rolls(self):
        self.rolls_allowed -= 1

    def reroll_authorized(self):
        return self.rolls_allowed > 0
    
    def count_values(self, value):
        return int(self.dice_set.count(value)*value)

    def count_brelan(self):
        counts = Counter(self.dice_set)
        for figure, value in counts.items():
            if value == 3:
                return(figure*value)
        return 0
    
    def count_carre(self):
        counts = Counter(self.dice_set)
        for figure, value in counts.items():
            if value == 4:
                return(figure*value)
        return 0
    
    def count_yahtzee(self):
        counts = Counter(self.dice_set)
        for _, value in counts.items():
            if value == 5:
                return 50
        return 0
    
    def count_full_house(self):
        counts = Counter(self.dice_set)
        if len(counts) == 2:
            if sorted(counts.values()) == [2,3]:
                return 25
        return 0
    
    def count_little_straight(self):
        sorted_values = sorted(self.dice_set)
        # Counter for consecutive numbers
        consecutive_count = 1

        for i in range(1, len(sorted_values)):
            # Check if the current value is consecutive to the previous one
            if sorted_values[i] == sorted_values[i - 1] + 1:
                consecutive_count += 1

                # Check if we have found four consecutive numbers
                if consecutive_count == 4:
                    return 30
            else:
                # Reset the counter if the sequence is broken
                consecutive_count = 1
        
        return 0

    def count_large_straight(self):
        sorted_values = sorted(self.dice_set)
        # Counter for consecutive numbers
        consecutive_count = 1

        for i in range(1, len(sorted_values)):
            # Check if the current value is consecutive to the previous one
            if sorted_values[i] == sorted_values[i - 1] + 1:
                consecutive_count += 1

                # Check if we have found four consecutive numbers
                if consecutive_count == 5:
                    return 40
            else:
                # Reset the counter if the sequence is broken
                consecutive_count = 1
        
        return 0
    
    def count_luck(self):
        return sum(self.dice_set)