from items import Armor
from player_info import Player
from world import Choice_World
class Interface:


    def __init__(self, choix, shield, sth2o, explorechoix, name, wname):
        Armor.shield = shield
        Armor.sth2o = sth2o
        Choice_World.wname = wname
        self.choix = choix
        Player.name = name
        self.explorechoix = explorechoix
        print('\nVous etes sur la planète, que voulez vous faire ?\n')
        print('1: Explorer')
        print('2: Voir ExoCombinaison')
        print('3: Exit')
        choix = input()

        if choix == "1":
            print('\n Explore :\n')
            print('Vous aller à la porte de votre Bunker...')
            print('Une voix robotique vous dit...')
            print('"Porte 23A closed !"')
            print('Résoudre l"énigme :')
            print('1 OU 3 ?')
            explorechoix = input()
            if explorechoix == "1":
                print('ERROR 404')
                print('1 OU 3 ?')
                explorechoix = input()
                if explorechoix == "3":
                    print('SUCCES. porte ouverte\n')
                    print(" \n ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒"
                    "░█▀█▀█░█▀██░█▀█░█▄█▄█░"
                    "░█▀█▀█░█▀████▀█░█▄█▄█░\n"
                    )
                    print("Vous sortez dehors !")
                    print(" \n ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒"
                    "░█▀█▀█░█▀██░█▀█░█▄█▄█░"
                    "░█▀█▀█░█▀████▀█░█▄█▄█░\n"
                    )
                    print(name, "vous voila sur la planète ", wname , "\n")
                    print("vous allez dans qu'elle direction ? \n")
                    print("NORD")
                    print("SUD")
                    print("EST")
                    print("OUEST")
                    choix = input()
                    if choix == "NORD":
                        print('..N.')
                    if choix == "SUD":
                        print('..S.')
                    if choix == "EST":
                        print('..E.')
                    if choix == "OUEST":
                        print('..O.')

            elif explorechoix == "3":
                print('SUCCES. porte ouverte\n')
                print(" \n ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒"
                "░█▀█▀█░█▀██░█▀█░█▄█▄█░"
                "░█▀█▀█░█▀████▀█░█▄█▄█░\n"
                )
                print("Vous sortez dehors !")
                print(" \n ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒"
                "░█▀█▀█░█▀██░█▀█░█▄█▄█░"
                "░█▀█▀█░█▀████▀█░█▄█▄█░\n"
                )
                print(name, "vous voila sur la planète ", wname , "\n")
                print("vous allez dans qu'elle direction ? \n")
                print("NORD")
                print("SUD")
                print("EST")
                print("OUEST")
                choix = input()
                if choix == "NORD":
                    print('..N.')
                if choix == "SUD":
                    print('..S.')
                if choix == "EST":
                    print('..E.')
                if choix == "OUEST":
                    print('..O.')



        if choix == "2":
            print('\n ExoCombinaison : \n')
            print('Exo Armor INFO : Statut Correct. Shield =', Armor.shield,'%', 'STH2O =', Armor.sth2o)
            print("STH2O = Système de traitement H2O")
        if choix == "3":
            print('Exit :')
            exit()
