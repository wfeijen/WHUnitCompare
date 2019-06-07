from unittest import TestCase
from src.Permutatie import Permutatie

# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestPermutatie(TestCase):

    def test___init1__(self):
        p1 = Permutatie()
        p2 = Permutatie().merge(p1)
        self.assertIsInstance(p2, Permutatie)
        self.assertEqual(p2.slotsGebruikt(), 0)

    def test___init1__(self):
        p1 = Permutatie()
        p1.merge({'key0': 1, 'key1': 2, 'key2': 3})
        p2 = Permutatie()
        p2.merge({'key1': 1, 'key2': 2, 'key3': 3})
        p2.merge(p1)
        self.assertIsInstance(p2, Permutatie)
        self.assertEqual(p2.slotsGebruikt(), 12)

