

from src.ModelMogelijkhedenList import ModelMogelijkhedenList
import numpy as np

class DamageOutputMatrixGenerator:
    def __init__(self, unitMogelijkhedenFile = "", weaponsFile = ""):
        self.modelModelijkhedenList = ModelMogelijkhedenList(unitMogelijkhedenFile, weaponsFile)
        self.modelBuildList = self.modelModelijkhedenList.createBuildList()

    # Dit is een simpele vergelijking waarin verondersteld wordt dat alle wapens gebruikt kunnen worden
    # Vervolgens worde alle saves zonder cover etc gedaan.
    def simpelMatrix(self):
        # create numpy array
        l = len(self.modelBuildList)
        self.array = np.zeros([l, l])

        for x, buildX in enumerate(self.modelBuildList):
            for y, buildY in enumerate(self.modelBuildList):
                self.array[x, y] = x + y
        return self.array

class DamageCalculator:
    def __init__(self, atacker, defender):
        self.atacker = atacker
        self.defender = defender

    def altijdAlleWapen(self):
        for weapon, number in self.atacker.weaponBuild:
            shots = 0
            for n in range(number):
                if weapon.type == "melee":
                    shots += self.atacker.modelEigenschappen.A.value()
                else:
                    shots += weapon.shots.value()
            hit = 0
            for shot in range(shots):
                i=1





