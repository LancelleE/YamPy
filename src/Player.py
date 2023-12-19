class Player:
    def __init__(self, playerName) -> None:
        self.playerName = playerName


        # Score Sheet
        # # Single numbers
        self.aces = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0

        # # Single numbers total
        self.minor = 0


        # # Single numbers bonus
        self.minor_bonus = 0

        # # Major
        self.three_of_a_kind = 0
        self.four_of_a_kind = 0
        self.full_house = 0
        self.small_straight = 0
        self.large_straight = 0
        self.yahtzee = 0
        self.chance = 0

        # # Major total
        self.major = 0

        # # Total
        self.total = 0
        
