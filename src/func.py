def choix_reroll():
    answer = input('Voulez-vous changer certains dés ? (Y/n)')
    while answer not in ['Y','n']:
        print("Choix invalide. Veuillez réessayer.")
        answer = input('Voulez-vous changer certains dés ? (Y/n)')
    
    return answer

def projection_score(player, dice, already_scored_list):
    pass