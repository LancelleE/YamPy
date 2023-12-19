from tabulate import tabulate, SEPARATING_LINE
class Game():
    def __init__(self, nb_players) -> None:
        self.nb_players = nb_players
        self.round = 0

    def set_players(self, players):
        self.players = players

    def new_round(self):
        self.round += 1

    def game_on(self):
        return self.round < 13
    
    def display_score(self):
        headers = [p.playerName for p in self.players]
        data = [
            ['1'] + [str(p.aces) for p in self.players],
            ['2'] + [str(p.twos) for p in self.players],
            ['3'] + [str(p.threes) for p in self.players],
            ['4'] + [str(p.fours) for p in self.players],
            ['5'] + [str(p.fives) for p in self.players],
            ['6'] + [str(p.sixes) for p in self.players],
            SEPARATING_LINE,
            ['Sous-total (hors bonus)'] + [str(p.minor_only) for p in self.players],
            ['Bonus (atteint si > 63)'] + [str(p.minor_bonus) for p in self.players],
            ['Sous-total (avec bonus)'] + [str(p.minor_and_bonus) for p in self.players],
            SEPARATING_LINE,
            ['Brelan'] + [str(p.three_of_a_kind) for p in self.players],
            ['Carré'] + [str(p.four_of_a_kind) for p in self.players],
            ['Full house'] + [str(p.full_house) for p in self.players],
            ['Petite suite'] + [str(p.small_straight) for p in self.players],
            ['Grande suite'] + [str(p.large_straight) for p in self.players],
            ['Yahtzee'] + [str(p.yahtzee) for p in self.players],
            ['Chance'] + [str(p.chance) for p in self.players],
            SEPARATING_LINE,
            ['Sous-total'] + [str(p.major) for p in self.players],
            SEPARATING_LINE,
            SEPARATING_LINE,
            ['Total'] + [str(p.total) for p in self.players]
        ]
        
        print(tabulate(data, headers=headers))
