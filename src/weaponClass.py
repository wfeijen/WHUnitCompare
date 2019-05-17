
#Weapon ;Range ;Type ;shots;S ;AP ;D ;Abilities
class Weapon:
    def __init__(self, stringIn = ""):
        strItems = stringIn.split(";")
        name = strItems[0]
        range = strItems[1]
        type = strItems[2]
        shots = strItems[4]
        s = strItems[5]
        AP = strItems[6]
        D = strItems[7]
        abilities = strItems[8]