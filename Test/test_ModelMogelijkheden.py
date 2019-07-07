from unittest import TestCase


from src.ModelMogelijkheden import ModelMogelijkheden
from src.WeaponsDict import WeaponsDict

# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestVariabele(TestCase):

    def test___init1__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        um = ModelMogelijkheden("1;c1;unit1;5;3;3;4;4;4;1;10;4;3;1|A", wd)
        self.assertIsInstance(um, ModelMogelijkheden)

    def test___init2__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        um = ModelMogelijkheden("1;c1;unit2;5;3;3;4;4;4;1;10;4;3;1-6|A,B", wd)
        self.assertIsInstance(um, ModelMogelijkheden)

    def test___init3__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        um = ModelMogelijkheden("1;c1;unit3;5;3;3;4;4;4;1;10;4;5;1-6|A,B[0-4|C,D]", wd)
        self.assertIsInstance(um, ModelMogelijkheden)

    def test___init4__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        um = ModelMogelijkheden("1;c2;unit4;5;3;3;4;4;4;1;10;4;6;1-6|A,B[0-4|C,[0-4|E,F][0-4|D]]", wd)
        self.assertIsInstance(um, ModelMogelijkheden)

    def test___init5__(self):
        wd = WeaponsDict("../Data/Weapons.csv")
        um = ModelMogelijkheden("1;c2;unit5;5;3;3;4;4;4;1;10;4;3;1-6|[0-3|A,B][0-3|C,D][0-3|E,F]", wd)
        self.assertIsInstance(um, ModelMogelijkheden)
