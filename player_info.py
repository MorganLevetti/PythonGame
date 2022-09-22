class Player:

    def __init__(self, name, health, attack, classe):
        self.name = name
        self.health = health
        self.attack = attack
        self.classe = classe
        print("Enter your name :")
        name = input()
        print("\nEnter your Class :")
        print("1: Capitaine")
        print("2: Ingénieur")
        print("3: Cannonier")
        classe = input()
        if classe == "1":
            print("\nVous avez choisi 'Capitaine', vous diriger l'expédition !")
        if classe == "2":
            print("\nVous avez choisi 'Ingénieur', la Mécanique est votre Dada !")
        if classe == "3":
            print("\nVous avez choisi 'Cannonier', explosion, munitions et extermination !")
        print('Bienvenue', name, 'Poste :',classe,'/ Point de vie:', health, 'Attaque: ', attack,'\n')

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack



      