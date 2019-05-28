from unittest import TestCase


from src.Variabele import Variabele

class TestVariabele(TestCase):
    def test___init1__(self):
        v = Variabele("d6")
        self.assertIsInstance(v,Variabele)

    def test___init2__(self):
        v = Variabele("6")
        self.assertIsInstance(v, Variabele)

    def test___init3__(self):
        v = Variabele("6d6")
        self.assertIsInstance(v, Variabele)

    def test___init4__(self):
        v = Variabele("10")
        self.assertIsInstance(v, Variabele)

    def test___init5__(self):
        v = Variabele("2d6")
        self.assertEqual(len(v) , 36)


    def test___init6__(self):
        self.assertRaises(ValueError, Variabele, ("x"))
        self.assertRaises(ValueError, Variabele, ("100"))



