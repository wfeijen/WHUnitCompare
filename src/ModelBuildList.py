# Maakt een lijst van unit builts op basis van een UnitMogelijkheden zodat alle mogelijke combinaties voorkomen.
from src.ModelBuild import ModelBuild

class ModelBuildList(list):
    def createUnitBuilds(self, unitMogelijkheden):
        weaponCombinations = unitMogelijkheden.weapons.permutationsOfGroupsInSameLevel()
        modelBuild = ModelBuild(unitMogelijkheden.modelEigenschappen)



    def __init__(self, unitMogelijkhedenList):
        for unitMogelijkheden in unitMogelijkhedenList:
            self.extend(self.createUnitBuilds(unitMogelijkheden))

