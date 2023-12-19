from src.Player import Player
from src.Dice import Dice

J1 = Player('etienne')
d = Dice()
print(f"""
      Le J1 est {J1.playerName}.\n
      Les dés ont donné : {d.D1}, {d.D2}, {d.D3}, {d.D4}, {d.D4}
""")
d.reroll('D1')
print(d.D1)