from os import wait3
from items import Armor

class Interface:


    def __init__(self, choix, shield, sth2o, explorechoix):
        Armor.shield = shield
        Armor.sth2o = sth2o
        self.choix = choix
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
            print('... Résoudre l"énigme :')
            print('1... OU 3 ?')
            explorechoix = input()
            if explorechoix == "1":
                print('ERROR 404')
                print('1... OU 3 ?')
                explorechoix = input()
                if explorechoix == "3":
                    print('SUCCES. porte ouverte')
            elif explorechoix == "3":
                print('SUCCES. porte ouverte')
        if choix == "2":
            print('\n ExoCombinaison : \n')
            print('Exo Armor INFO : Statut Correct. Shield =', Armor.shield,'%', 'STH2O =', Armor.sth2o)
            print("STH2O = Système de traitement H2O")
        if choix == "3":
            print('Exit :')
            exit()
