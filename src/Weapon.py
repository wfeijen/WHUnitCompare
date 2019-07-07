from src.ValueList import ValueList
import re


#Cost,Codex, Weapon ;Range ;Type shots;S ;AP ;D ;Abilities
class Weapon:
    def __init__(self, stringIn):
        stringZonderTekens = re.sub('["]', '', stringIn.lower())
        stringDelen = re.sub(' *; *', ';', stringZonderTekens).split(";")
        self.maxOccurrences = 100 # Om later binnen weapongrouping op te kunnen sorteren

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
                self.shots = ValueList("0")
                self.shots.AttacksUser = True
            else:
                self.type = strTypeShots[0]
                self.shots = ValueList(strTypeShots[1])
                self.shots.AttacksUser = False

            field = field - 1
            strRange = stringDelen[field].split("-")
            if re.match("^melee", strRange[0]):
                self.range = (0, 0)
            elif len(strRange)>1:
                self.range = (int(strRange[0]), int(strRange[1]))
            elif re.match("^pistol", self.type):
                self.range = (0, int(strRange[0]))
            else:
                self.range = (1, int(strRange[0]))

            field = field + 2
            if re.match("^user", stringDelen[field]):
                self.S  = ValueList("0")
                self.S.efectModelStrengt = "+"
            elif re.match("^\*", stringDelen[field]):
                self.S  = ValueList("0")
                self.S.efectModelStrengt = "*"
            elif re.match("^[+x]", stringDelen[field]):
                self.S  = ValueList(stringDelen[field][1:])
                self.S.efectModelStrengt = stringDelen[field][0]
            else:
                self.S = ValueList(stringDelen[field])
                self.S.efectModelStrengt = ""

            field = field + 1
            self.AP = ValueList(stringDelen[field].replace("-", ""))
            field = field + 1
            self.D = ValueList(stringDelen[field])
            field = field + 1
            self.abilities = stringDelen[field]
        except ValueError as e:
            print("############")
            print("     De volgende wapenregel kon niet verwerkt worden: ", stringIn)
            print("     Het betreft veld:", field, "tellend vanaf 0")
            print("     De foutmelding is:", e.args)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return str(self.name)

