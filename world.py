class Choice_World:
    def __init__(self, niveau, wname):
        self.niveau = niveau
        self.wname = wname
        print("Choice World:")
        print("1 : ")
        print("2 : ")
        print("3 : ")
        niveau = input()
        if niveau == "1":
            print("Enter Name World1 :")
            wname = input()
            print("\nBienvenue sur la planète", wname)
        elif niveau == "2":
            print("Enter Name World2 :")
            wname = input()
            print("\nBienvenue sur la planète", wname)
        elif niveau == "3":
            print("Enter Name World3 :")
            wname = input()
            print("\nBienvenue sur la planète", wname)
        else:
            print('Incorrect')
    