from src.Variabele import Variabele
from src.WeaponGrouping import WeaponGrouping


# Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons

class UnitMogelijkheden:
    def __init__(self, stringIn, wd):
        stringDelen = stringIn.lower().split(";")
        i = 0
        self.Codex = stringDelen[i]
        i = i + 1
        self.Unit = stringDelen[i]
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
        self.Save = Variabele(stringDelen[i])
        i = i + 1
        self.Inv = Variabele(stringDelen[i])
        i = i + 1
        self.Weapons = WeaponGrouping( stringDelen[i], wd)