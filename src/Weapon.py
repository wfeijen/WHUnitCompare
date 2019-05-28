from src.Variabele import Variabele
import re


#Cost,Codex, Weapon ;Range ;Type shots;S ;AP ;D ;Abilities
class Weapon:
    def __init__(self, stringIn):
        stringZonderTekens = re.sub('["]', '', stringIn.lower())
        stringDelen = re.sub(' *; *', ';', stringZonderTekens).split(";")
        field = 0
        self.cost = int(stringDelen[field])
        field = field + 1
        self.codex = stringDelen[field]
        field = field + 1
        self.name = stringDelen[field]
        try:
            field = field + 2
            strTypeShots = stringDelen[field].split(" ")
            if re.match("^melee", strTypeShots[0]):
                self.type = "melee"
                self.shots = Variabele("0")
                self.shots.AttacksUser = True
            else:
                self.type = strTypeShots[0]
                self.shots = Variabele(strTypeShots[1])
                self.shots.AttacksUser = False

            field = field - 1
            strRange = stringDelen[field].split("-")
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
            if re.match("^user", stringDelen[field]):
                self.S  = Variabele("0")
                self.S.efectModelStrengt = "+"
            elif re.match("^\*", stringDelen[field]):
                self.S  = Variabele("0")
                self.S.efectModelStrengt = "*"
            elif re.match("^[+x]", stringDelen[field]):
                self.S  = Variabele(stringDelen[field][1:])
                self.S.efectModelStrengt = stringDelen[field][0]
            else:
                self.S = Variabele(stringDelen[field])
                self.S.efectModelStrengt = ""

            field = field + 1
            self.AP = Variabele(stringDelen[field].replace("-",""))
            field = field + 1
            self.D = Variabele(stringDelen[field])
            field = field + 1
            self.abilities = stringDelen[field]
        except ValueError as e:
            print("############")
            print("     De volgende wapenregel kon niet verwerkt worden: ", stringIn)
            print("     Het betreft veld:", field, "tellend vanaf 0")
            print("     De foutmelding is:", e.args)

