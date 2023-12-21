from tabulate import tabulate
class Player:
    # Score Sheet
    # # Single numbers
    aces = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    # # Single numbers total
    minor_only = 0

    # # Single numbers bonus
    minor_bonus = 0

    # # Single numbers and bonus
    minor_and_bonus = 0

    # # Major
    three_of_a_kind = 0
    four_of_a_kind = 0
    full_house = 0
    small_straight = 0
    large_straight = 0
    yahtzee = 0
    chance = 0

    # # Major total
    major = 0

    # # Total
    total = 0

    already_scored = []
    scorable = ['1','2','3','4','5','6','Brelan','Carré','Full','Petite suite','Grande suite','Yam','Chance']

    association = {
        '1': 'aces',
        '2': 'twos',
        '3': 'threes',
        '4': 'fours',
        '5': 'fives',
        '6': 'sixes',
        'Brelan': 'three_of_a_kind',
        'Carré': 'four_of_a_kind',
        'Full': 'full_house',
        'Petite suite': 'small_straight',
        'Grande suite': 'large_straight',
        'Yam': 'yahtzee',
        'Chance': 'chance'
    }

    def __init__(self, playerName) -> None:
        self.playerName = playerName

    def get_score(self):
        data = [
            ['1', self.aces],
            ['2', self.twos],
            ['3', self.threes],
            ['4', self.fours],
            ['5', self.fives],
            ['6', self.sixes],
            ['-- Sous-total', self.minor],
            ['-- Bonus', self.minor_bonus],
            ['Brelan', self.three_of_a_kind],
            ['Carré', self.four_of_a_kind],
            ['Full', self.full_house],
            ['Petite suite', self.small_straight],
            ['Grande suite', self.large_straight],
            ['Yam', self.yahtzee],
            ['Chance', self.chance],
            ['-- Sous-total', self.major],
            ['----Total', self.total]
        ]
        headers = ['Figure','Score']
        print(tabulate(data, headers=headers, tablefmt="rounded_outline"))

    def refresh_bonuses(self):
        self.minor_only = sum([self.aces, self.twos, self.threes, self.fours, self.fives, self.sixes])
        self.minor_bonus = 35 if self.minor_only >= 63 else 0
        self.minor_and_bonus = self.minor_only + self.minor_bonus

        self.major = sum([self.three_of_a_kind, self.four_of_a_kind, self.full_house, self.small_straight, self.large_straight, self.yahtzee, self.chance])
        self.total = self.minor_and_bonus + self.major

    



    



        
