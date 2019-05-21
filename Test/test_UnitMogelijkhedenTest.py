from unittest import TestCase

from src.UnitMogelijkhedenList import UnitMogelijkhedenList

class TestWeaponsList(TestCase):
    def test___init1__(self):
        uml = UnitMogelijkhedenList("../Data/Units.csv", "../Data/Weapons.csv")
        self.assertIsInstance(uml, UnitMogelijkhedenList)

