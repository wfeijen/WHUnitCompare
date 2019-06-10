from unittest import TestCase
from src.Permutation import Permutation

# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestPermutatie(TestCase):

    def test___init1__(self):
        p1 = Permutation()
        p2 = Permutation().merge(p1)
        self.assertIsInstance(p2, Permutation)
        self.assertEqual(p2.slotsGebruikt(), 0)

    def test___init1__(self):
        p1 = Permutation()
        p1.merge({'key0': 1, 'key1': 2, 'key2': 3})
        p2 = Permutation()
        p2.merge({'key1': 1, 'key2': 2, 'key3': 3})
        p2.merge(p1)
        self.assertIsInstance(p2, Permutation)
        self.assertEqual(p2.slotsGebruikt(), 12)
