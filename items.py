class Capsule:

    def __init__(self, oxygene, gravity, temp, carbonne):
        self.oxygene = oxygene
        self.gravity = gravity
        self.temp = temp
        self.carbonne = carbonne
        print('INFO CAPSULE : Oxy =', oxygene,'% ' 'Grav =', gravity, 'Temp Extérieur =', temp, 'Carb Présent TRUE =', carbonne)

class Armor:

    def __init__(self, shield, sth2o, oxygene):
        self.shield = shield
        self.sth2o = sth2o
        if oxygene > 50:
            print('Exo Armor INFO : Statut Correct. Shield =', shield,'%', 'STH2O =', sth2o)
            print("STH2O = Système de traitement H2O")
        if 40 > oxygene > 10:
            print('Exo Armor INFO : Statut Moyen. Shield =', shield,'%', 'STH2O =', sth2o)
            print("Oxygène Inférieur à 50% :", oxygene, '% RECHARGE !')
        else:
            print('Exo Info Clear')