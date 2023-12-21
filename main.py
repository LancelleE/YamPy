from src.Player import Player
from src.Dice import Dice
from src.Game import Game
from src.func import choix_reroll, projection_score

if __name__ == '__main__':
    nb_player = int(input('How many players ?\n'))
    game = Game(nb_player)
    print(f'Nous allons jouer à {game.nb_players} joueurs !\n')

    players = []
    for i in range(game.nb_players):
        name = input(f'Name of Player {i+1} : ')
        players.append(Player(name))

    game.set_players(players)

    while game.game_on():

        game.new_round()
        game.display_score()

        print(f'Round {game.round}')
        for p in game.players:
            print(f'Au tour de {p.playerName} !\n')
            # p.get_score()
            dice = Dice()
            dice.announce_dices()
            projection_score(p, dice)


            while choix_reroll() == 'Y':
                if dice.reroll_authorized():
                    nb_reroll = int(input('Nombre de dés à relancer : \n'))
                    if nb_reroll > 0:
                        dice.decrease_rolls()
                        for _ in range(nb_reroll):
                            change = input('Quel dé changer ? Ecrire par exemple D1 pour le dé 1.\n')
                            dice.reroll(change)
                        dice.announce_dices()
                        projection_score(p, dice)
                else:
                    break
                    
            else:
                print('coucou')
                projection_score(p, dice)
                # Demander à scorer
            
                dice.announce_dices()


            break
        break
