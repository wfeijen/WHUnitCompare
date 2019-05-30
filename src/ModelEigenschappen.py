from src.Variabele import Variabele

class ModelEigenschappen:
    def __init__(self, stringDelen):
        i = 0
        self.cost = int(stringDelen[i])
        i = i + 1
        self.codex = stringDelen[i]
        i = i + 1
        self.unit = stringDelen[i]
        i = i + 1
        self.M = Variabele(stringDelen[i])
        i = i + 1
        self.WS = Variabele(stringDelen[i])
        i = i + 1
        self.BS = Variabele(stringDelen[i])
        i = i + 1
        self.S = Variabele(stringDelen[i])
        i = i + 1
        self.T = Variabele(stringDelen[i])
        i = i + 1
        self.W = Variabele(stringDelen[i])
        i = i + 1
        self.A = Variabele(stringDelen[i])
        i = i + 1
        self.Ld = Variabele(stringDelen[i])
        i = i + 1
        self.save = Variabele(stringDelen[i])
        i = i + 1
        self.Inv = Variabele(stringDelen[i])