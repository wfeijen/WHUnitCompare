#1|A
#1-6|A,B
#1-6|A,B[0-4|C,D]
#1-6|A,B[0-4|C,[0-4|E,F][0-4|D]]
#1-6|[0-3|A,B][0-3|C,D][0-3|E,F]

from unittest import TestCase

from src.WeaponsDict import WeaponsDict
from src.WeaponGrouping import WeaponGrouping


class TestWeaponGrouping(TestCase):
    def test___init1__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1|A".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)
        permutaties = wg.permutaties(0, 1000,0)
        self.assertIsInstance(permutaties, list)
        sg = permutaties[0].slotsGebruikt()
        self.assertEqual(sg, 1)

    def test___init2__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1-6|a".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)
        permutaties = wg.permutaties(0, 1000,0)
        self.assertIsInstance(permutaties, list)
        sg = permutaties[0].slotsGebruikt()
        self.assertEqual(sg, 1)

    def test___init3__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1-6|A,B".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)
        permutaties = wg.permutaties(0, 1000,0)
        self.assertIsInstance(permutaties, list)
        sg = permutaties[0].slotsGebruikt()
        self.assertEqual(sg, 1)

    def test___init3b__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1-6|A,B,C".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)
        permutaties = wg.permutaties(0, 1000,0)
        self.assertIsInstance(permutaties, list)
        sg = permutaties[0].slotsGebruikt()
        self.assertEqual(sg, 1)

    def test___init3c__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("0-6|A,B,C".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)
        permutaties = wg.permutaties(0, 1000, 0)
        self.assertIsInstance(permutaties, list)
        sg = permutaties[0].slotsGebruikt()
        self.assertEqual(sg, 0)

    def test___init4__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1-6|A,B[0-4|C,D]".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)

    def test___init5__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1-6|A,B[0-4|C,[0-4|E,F][0-4|D]]".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)

    def test___init6__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        wg = WeaponGrouping("1-6|[0-2|A,B][0-3|C,D][0-5|E,F]".lower(), wd)
        self.assertIsInstance(wg, WeaponGrouping)