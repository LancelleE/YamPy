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
    minor = 0


    # # Single numbers bonus
    minor_bonus = 0

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

    def __init__(self, playerName) -> None:
        self.playerName = playerName



        
