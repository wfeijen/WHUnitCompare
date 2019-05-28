from unittest import TestCase


from src.UnitMogelijkhedenList import UnitMogelijkhedenList

# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestVariabele(TestCase):

    def test___init1__(self):
        uml = UnitMogelijkhedenList(unitMogelijkhedenFile = "../Data/Units.csv", weaponsFile = "../Data/Weapons.csv")
        self.assertIsInstance(uml, UnitMogelijkhedenList)

    def test___init1__(self):
        uml = UnitMogelijkhedenList(unitMogelijkhedenFile = "../Data/Units1.csv", weaponsFile = "../Data/Weapons1.csv")
        self.assertIsInstance(uml, UnitMogelijkhedenList)