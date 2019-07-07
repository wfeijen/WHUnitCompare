from unittest import TestCase


from src.ValueList import ValueList

class TestVariabele(TestCase):
    def test___init1__(self):
        v = ValueList("d6")
        self.assertIsInstance(v, ValueList)

    def test___init2__(self):
        v = ValueList("6")
        self.assertIsInstance(v, ValueList)

    def test___init3__(self):
        v = ValueList("6d6")
        self.assertIsInstance(v, ValueList)

    def test___init4__(self):
        v = ValueList("10")
        self.assertIsInstance(v, ValueList)

    def test___init5__(self):
        v = ValueList("2d6")
        self.assertEqual(len(v) , 36)


    def test___init6__(self):
        self.assertRaises(ValueError, ValueList, ("x"))
        self.assertRaises(ValueError, ValueList, ("100"))



