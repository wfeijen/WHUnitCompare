from unittest import TestCase


from src.Variabele import Variabele

class TestVariabele(TestCase):
    def test___init1__(self):
        v = Variabele("d6")
        self.assertIsInstance(v,Variabele)
        v = Variabele("6")
        self.assertIsInstance(v, Variabele)
        v = Variabele("6d6")
        self.assertIsInstance(v, Variabele)
        v = Variabele("10")
        self.assertIsInstance(v, Variabele)
        v = Variabele("2d6")
        self.assertEqual(len(v.waarde) , 36)


    def test___init2__(self):
        self.assertRaises(ValueError, Variabele, ("x"))
        self.assertRaises(ValueError, Variabele, ("100"))
        self.assertRaises(ValueError, Variabele, (""))



