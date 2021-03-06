from unittest import TestCase

from src.Weapon import Weapon
# Cost;Codex;Weapon ;Range ;Type en shots;S ;AP ;D ;Abilities

class TestWeapon(TestCase):
    def test___init1__(self):
        w = Weapon('1;Tau;A;Melee;Melee ;User ;2;1;')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "melee")
        self.assertEqual(w.shots, [0])
        self.assertEqual(w.shots.AttacksUser, True)
        self.assertEqual(w.range, (0, 0))
        self.assertEqual(w.S, [0])
        self.assertEqual(w.S.efectModelStrengt, "+")
        self.assertEqual(w.AP, [2])
        self.assertEqual(w.D, [1])
        self.assertEqual(w.cost, 1)

    def test___init2__(self):
        w = Weapon('2;Tau;Plagueburst Mortar;12"-48";Heavy D6;8;-2;D3;Plague Weapon. This weapon can target units that are not visible to the bearer.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "heavy")
        self.assertEqual(w.shots, [1,2,3,4,5,6])
        self.assertEqual(w.shots.AttacksUser, False)
        self.assertEqual(w.range, (12,48))
        self.assertEqual(w.S, [8])
        self.assertEqual(w.S.efectModelStrengt, "")
        self.assertEqual(w.AP, [2])
        self.assertEqual(w.D, [1,2,3])
        self.assertEqual(w.cost, 2)

    def test___init3__(self):
        w = Weapon('3;Tau;Improvised weapon;Melee;Melee;User;0;1;-')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "melee")
        self.assertEqual(w.shots, [0])
        self.assertEqual(w.shots.AttacksUser, True)
        self.assertEqual(w.range, (0,0))
        self.assertEqual(w.S, [0])
        self.assertEqual(w.S.efectModelStrengt, "+")
        self.assertEqual(w.AP, [0])
        self.assertEqual(w.D, [1])
        self.assertEqual(w.cost, 3)

    def test___init4__(self):
        w = Weapon('4;Tau;Plaguespitter;9";Assault D6;User;-1;1;Plague Weapon.This weapon automatically hits its target.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "assault")
        self.assertEqual(w.shots, [1,2,3,4,5,6])
        self.assertEqual(w.shots.AttacksUser, False)
        self.assertEqual(w.range, (1, 9))
        self.assertEqual(w.S, [0])
        self.assertEqual(w.S.efectModelStrengt, "+")
        self.assertEqual(w.AP, [1])
        self.assertEqual(w.D, [1])
        self.assertEqual(w.cost, 4)

    def test___init5__(self):
        w = Weapon('5;Tau;Injector pistol;3";Pistol 1;4;-1;D6;Plague Weapon. This weapon\'s damage changes to 1 when attacking VEHICLES.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "pistol")
        self.assertEqual(w.shots, [1])
        self.assertEqual(w.shots.AttacksUser, False)
        self.assertEqual(w.range, (0, 3))
        self.assertEqual(w.S, [4])
        self.assertEqual(w.S.efectModelStrengt, "")
        self.assertEqual(w.AP, [1])
        self.assertEqual(w.D, [1,2,3,4,5,6])
        self.assertEqual(w.cost, 5)

    def test___init6__(self):
        w = Weapon('6;Tau;Hyper Blight Grenades;6";Grenade D6;4;0;2;Plague Weapon. Each wound roll of 6+ made for this weapon inflicts a mortal wound in addition to any other damage.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "grenade")
        self.assertEqual(w.shots, [1,2,3,4,5,6])
        self.assertEqual(w.shots.AttacksUser, False)
        self.assertEqual(w.range, (1, 6))
        self.assertEqual(w.S, [4])
        self.assertEqual(w.S.efectModelStrengt, "")
        self.assertEqual(w.AP, [0])
        self.assertEqual(w.D, [2])
        self.assertEqual(w.cost, 6)

    def test___init7__(self):
        w = Weapon('7;Tau;Bubotic Axe;Melee;Melee;+1;-2;1;You can re-roll wound rolls of 1 for this weapon.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "melee")
        self.assertEqual(w.shots, [0])
        self.assertEqual(w.shots.AttacksUser, True)
        self.assertEqual(w.range, (0, 0))
        self.assertEqual(w.S, [1])
        self.assertEqual(w.S.efectModelStrengt, "+")
        self.assertEqual(w.AP, [2])
        self.assertEqual(w.D, [1])
        self.assertEqual(w.cost, 7)

    def test___init8__(self):
        w = Weapon('8;Tau;Great plague cleaver;Melee;Melee;x2;-3;D6;When attacking with this weapon, you must subtract 1 from the hit roll. You can re-roll wound rolls of 1 for this weapon.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "melee")
        self.assertEqual(w.shots, [0])
        self.assertEqual(w.shots.AttacksUser, True)
        self.assertEqual(w.range, (0, 0))
        self.assertEqual(w.S, [2])
        self.assertEqual(w.S.efectModelStrengt, "x")
        self.assertEqual(w.AP, [3])
        self.assertEqual(w.D, [1,2,3,4,5,6])
        self.assertEqual(w.cost, 8)

    def test___init9__(self):
        w = Weapon(
            '9;Tau;Contagion spray;9";Pistol 2D3;*;-2;1;Attacks made with this weapon automatically hit the selected target. This weapon always wounds on a result of a 2+ unless the target unit has the VEHICLE keyword, in which case a result of 6+ is required.')
        self.assertIsInstance(w, Weapon)
        self.assertEqual(w.type, "pistol")
        self.assertEqual(w.shots, [2,3,4,3,4,5,4,5,6])
        self.assertEqual(w.shots.AttacksUser, False)
        self.assertEqual(w.range, (0, 9))
        self.assertEqual(w.S, [0])
        self.assertEqual(w.S.efectModelStrengt, "*")
        self.assertEqual(w.AP, [2])
        self.assertEqual(w.D, [1])
        self.assertEqual(w.cost, 9)