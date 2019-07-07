from src.ValueList import ValueList

class ModelEigenschappen:
    def __init__(self, stringDelen):
        i = 0
        self.cost = int(stringDelen[i])
        i = i + 1
        self.codex = stringDelen[i]
        i = i + 1
        self.unit = stringDelen[i]
        i = i + 1
        self.M = ValueList(stringDelen[i])
        i = i + 1
        self.WS = ValueList(stringDelen[i])
        i = i + 1
        self.BS = ValueList(stringDelen[i])
        i = i + 1
        self.S = ValueList(stringDelen[i])
        i = i + 1
        self.T = ValueList(stringDelen[i])
        i = i + 1
        self.W = ValueList(stringDelen[i])
        i = i + 1
        self.A = ValueList(stringDelen[i])
        i = i + 1
        self.Ld = ValueList(stringDelen[i])
        i = i + 1
        self.save = ValueList(stringDelen[i])
        i = i + 1
        self.Inv = ValueList(stringDelen[i])