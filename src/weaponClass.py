from src.variabeleClass import Variabele
import re


#Weapon ;Range ;Type shots;S ;AP ;D ;Abilities
class Weapon:
    def __init__(self, stringIn = ""):
        strItems = stringIn.replace('"', '').lower().split(";")
        self.name = strItems[0]

        strTypeShots = strItems[2].split(" ")
        if re.match("^melee", strTypeShots[0]):
            self.type = "melee"
            self.shots = Variabele("0")
            self.shots.AttacksUser = True
        else:
            self.type = strTypeShots[0]
            self.shots = Variabele(strTypeShots[1])
            self.shots.AttacksUser = False

        strRange = strItems[1].split("-")
        if re.match("^melee", strRange[0]):
            self.rangeMin = Variabele("0")
            self.rangeMax = Variabele("0")
        elif len(strRange)>1:
            self.rangeMax = Variabele(strRange[1])
            self.rangeMin = Variabele(strRange[0])
        elif re.match("^pistol", self.type):
            self.rangeMin = Variabele("0")
            self.rangeMax = Variabele(strRange[0])
        else:
            self.rangeMin = Variabele("1")
            self.rangeMax = Variabele(strRange[0])

        if re.match("^user", strItems[3]):
            self.S  = Variabele("0")
            self.S.efectModelStrengt = "+"
        elif re.match("^\*", strItems[3]):
            self.S  = Variabele("0")
            self.S.efectModelStrengt = "*"
        elif re.match("^[+x]", strItems[3]):
            self.S  = Variabele(strItems[3][1:])
            self.S.efectModelStrengt = strItems[3][0]
        else:
            self.S = Variabele(strItems[3])
            self.S.efectModelStrengt = ""

        self.AP = Variabele(strItems[4].replace("-",""))
        self.D = Variabele(strItems[5])
        self.abilities = strItems[6]