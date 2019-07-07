from unittest import TestCase


from src.ModelMogelijkhedenList import ModelMogelijkhedenList

# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestVariabele(TestCase):

    def test___creation__(self):
        uml = ModelMogelijkhedenList(unitMogelijkhedenFile ="../Data/Units.csv", weaponsFile ="../Data/Weapons.csv")
        self.assertIsInstance(uml, ModelMogelijkhedenList)

    def test___creation2__(self):
        uml = ModelMogelijkhedenList(unitMogelijkhedenFile ="../Data/Units1.csv", weaponsFile ="../Data/Weapons1.csv")
        self.assertIsInstance(uml, ModelMogelijkhedenList)

    def test___buildList1__(self):
        uml = ModelMogelijkhedenList(unitMogelijkhedenFile ="../Data/Units.csv", weaponsFile ="../Data/Weapons.csv")
        bl = uml.createBuildList()
        self.assertIsInstance(bl, list)

    def test___buildList2__(self):
        uml = ModelMogelijkhedenList(unitMogelijkhedenFile="../Data/Units1.csv", weaponsFile="../Data/Weapons1.csv")
        bl = uml.createBuildList()
        self.assertIsInstance(bl, list)