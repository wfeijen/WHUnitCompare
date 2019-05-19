from unittest import TestCase

from src.WeaponsDict import WeaponsDict

class TestWeaponsList(TestCase):
    def test___init1__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        self.assertIsInstance(wd, WeaponsDict)

    def test___init1__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        w = wd.weapons['a']
        self.assertEqual('a', w.name)