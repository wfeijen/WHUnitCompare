from src.ModelEigenschappen import ModelEigenschappen
from src.WeaponGrouping import WeaponGrouping
import re

class UnitMogelijkheden:
    def __init__(self, stringIn, wd):
        stringZonderTekens = re.sub('[+"]', '',stringIn.lower())
        stringDelen = re.sub(' *; *', ';',stringZonderTekens).split(";")
        self.modelEigenschappen = ModelEigenschappen(stringDelen[:13])
        self.weapons = WeaponGrouping( stringDelen[13], wd)