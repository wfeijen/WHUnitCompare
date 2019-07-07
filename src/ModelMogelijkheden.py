from src.ModelEigenschappen import ModelEigenschappen
from src.WeaponGrouping import WeaponGrouping
from src.ModelBuild import ModelBuild

import re

class ModelMogelijkheden:
    def __init__(self, stringIn, wd):
        stringZonderTekens = re.sub('[+"]', '',stringIn.lower())
        stringDelen = re.sub(' *; *', ';',stringZonderTekens).split(";")
        self.modelEigenschappen = ModelEigenschappen(stringDelen[:13])
        self.weapons = WeaponGrouping( stringDelen[13], wd)

    def createBuildList(self):
        modelBuildList = []
        weaponPermutations = self.weapons.permutations()
        for weaponPermutation in weaponPermutations:
            modelBuild = ModelBuild(self.modelEigenschappen, weaponPermutation)
            modelBuildList.append(modelBuild)
        return modelBuildList
