from unittest import TestCase

from src.variabeleClass import Variabele

class TestVariabele(TestCase):
    def test___init1__(self):
        v = Variabele("d1")
        self.assertIsInstance(v,Variabele)

    def test___init2__(self):
        self.assertRaises(ValueError, Variabele, ("x"))
        self.assertRaises(ValueError, Variabele, ("100"))
        self.assertRaises(ValueError, Variabele, (""))



