from player_info import Player
from items import Capsule
from items import Armor
from world import Choice_World
from interface import Interface



# Player 1 Infos (Name, Health, Attack)
print(  "╔╗╔╗╔═╗╔╗─╔╗─╔═╗\n"
        "║╚╝║║╦╝║║─║║─║║║\n"
        "║╔╗║║╩╗║╚╗║╚╗║║║\n"
        "╚╝╚╝╚═╝╚═╝╚═╝╚═╝\n")
player1 = Player("", 20, 4, "")
# Player 2 Info
# player2 = Player("", 20, 2, "")

world1 = Choice_World("", "")


print(" \n ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒"
                "░█▀█▀█░█▀██░█▀█░█▄█▄█░"
                "░█▀█▀█░█▀████▀█░█▄█▄█░"
                "████████▀█████████████\n"
                )
# Capsule Info (Oxygene, Gravity, Température, Carbonne)
status1 = Capsule(100, 20, -10, 2.0)
# Armure Info (Shield, STH2O, StatOxygene )
armor1 = Armor(100, 5.0, status1.oxygene)
print(" \n ▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒"
                "░█▀█▀█░█▀██░█▀█░█▄█▄█░"
                "░█▀█▀█░█▀████▀█░█▄█▄█░"
                "████████▀█████████████\n"
                )

interface = Interface("", armor1.shield, armor1.sth2o, "", player1.name, world1.wname)



        
