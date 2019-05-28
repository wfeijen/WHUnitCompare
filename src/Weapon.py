from src.Variabele import Variabele
import re


#Cost,Codex, Weapon ;Range ;Type shots;S ;AP ;D ;Abilities
class Weapon:
    def __init__(self, stringIn):
        strItems = stringIn.replace('"', '').lower().split(";")
        field = 0
        self.cost = int(strItems[field])
        field = field + 1
        self.codex = strItems[field]
        field = field + 1
        self.name = strItems[field]
        try:
            field = field + 2
            strTypeShots = strItems[field].split(" ")
            if re.match("^melee", strTypeShots[0]):
                self.type = "melee"
                self.shots = Variabele("0")
                self.shots.AttacksUser = True
            else:
                self.type = strTypeShots[0]
                self.shots = Variabele(strTypeShots[1])
                self.shots.AttacksUser = False

            field = field - 1
            strRange = strItems[field].split("-")
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

            field = field + 2
            if re.match("^user", strItems[field]):
                self.S  = Variabele("0")
                self.S.efectModelStrengt = "+"
            elif re.match("^\*", strItems[field]):
                self.S  = Variabele("0")
                self.S.efectModelStrengt = "*"
            elif re.match("^[+x]", strItems[field]):
                self.S  = Variabele(strItems[field][1:])
                self.S.efectModelStrengt = strItems[field][0]
            else:
                self.S = Variabele(strItems[field])
                self.S.efectModelStrengt = ""

            field = field + 1
            self.AP = Variabele(strItems[field].replace("-",""))
            field = field + 1
            self.D = Variabele(strItems[field])
            field = field + 1
            self.abilities = strItems[field]
        except ValueError as e:
            print("############")
            print("     De volgende wapenregel kon niet verwerkt worden: ", stringIn)
            print("     Het betreft veld:", field, "tellend vanaf 0")
            print("     De foutmelding is:", e.args)

