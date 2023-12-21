from tabulate import tabulate


def choix_reroll():
    answer = input('Voulez-vous changer certains dés ? (Y/n)\n')
    while answer not in ['Y','n']:
        print("Choix invalide. Veuillez réessayer.\n")
        answer = input('Voulez-vous changer certains dés ? (Y/n)\n')
    
    return answer

def projection_score(player, dice):
    data = [
            ['1', f'(+{dice.count_values(1)})' if '1' not in player.already_scored else player.aces],
            ['2', f'(+{dice.count_values(2)})' if '2' not in player.already_scored else player.twos],
            ['3', f'(+{dice.count_values(3)})' if '3' not in player.already_scored else player.threes],
            ['4', f'(+{dice.count_values(4)})' if '4' not in player.already_scored else player.fours],
            ['5', f'(+{dice.count_values(5)})' if '5' not in player.already_scored else player.fives],
            ['6', f'(+{dice.count_values(6)})' if '6' not in player.already_scored else player.sixes],
            ['-- Sous-total', ''],
            ['-- Bonus', ''],
            ['Brelan', f'(+{dice.count_brelan()})' if 'Brelan' not in player.already_scored else player.three_of_a_kind],
            ['Carré', f'(+{dice.count_carre()})' if 'Carré' not in player.already_scored else player.four_of_a_kind],
            ['Full', f'(+{dice.count_full_house()})' if 'Full' not in player.already_scored else player.full_house],
            ['Petite suite', f'(+{dice.count_little_straight()})' if 'Petite suite' not in player.already_scored else player.small_straight],
            ['Grande suite', f'(+{dice.count_large_straight()})' if 'Grande suite' not in player.already_scored else player.large_straight],
            ['Yam', f'(+{dice.count_yahtzee()})' if 'Yam' not in player.already_scored else player.yahtzee],
            ['Chance', f'(+{dice.count_luck()})' if 'Chance' not in player.already_scored else player.chance],
            ['-- Sous-total', ''],
            ['----Total', '']
        ]
    headers = ['Figure','Score']
    print(tabulate(data, headers=headers, tablefmt="rounded_outline"))
    

def score(player, dice, figure):
    
    pass
