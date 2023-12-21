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
    
def choix_figure_score(player):
    figure = input('Quelle figure scorer ? Ecrire en toute lettre comme dans la tableau du dessus.\n')
    while figure not in player.scorable:
        print('Choix incorrect.\n')
        figure = input('Quelle figure scorer ? Ecrire en toute lettre comme dans la tableau du dessus.\n')
    while figure in player.already_scored:
        print('Tu as déjà scoré cette figure.')
        figure = input('Quelle figure scorer ? Ecrire en toute lettre comme dans la tableau du dessus.\n')

    return figure

def choice_function(figure, dice):
    actions = {
        '1': lambda: dice.count_values(1),
        '2': lambda: dice.count_values(2),
        '3': lambda: dice.count_values(3),
        '4': lambda: dice.count_values(4),
        '5': lambda: dice.count_values(5),
        '6': lambda: dice.count_values(6),
        'Brelan': lambda: dice.count_brelan(),
        'Carré': lambda: dice.count_carre(),
        'Full': lambda: dice.count_full_house(),
        'Petite suite': lambda: dice.count_little_straight(),
        'Grande suite': lambda: dice.count_large_straight(),
        'Yam': lambda: dice.count_yahtzee(),
        'Chance': lambda: dice.count_luck()
    }

    if figure in actions:
        result = actions[figure]()  # Appelle la fonction correspondante
        # print(f"Résultat pour '{figure}': {result}")  # Affichage pour débogage
        return result
    else:
        print(f"La clé '{figure}' n'est pas reconnue.")
        return None
    

def score(player, de, figure):
    print(f'La figure à scorer est ' + figure)
    valeur = choice_function(figure, de)
    print(valeur)
    setattr(player, player.association[figure], valeur)
    player.already_scored.append(figure)
