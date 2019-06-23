from unittest import TestCase
from src.Permutation import Permutation

# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestPermutatie(TestCase):

    def test___merge1__(self):
        p1 = Permutation()
        p2 = Permutation()
        p2.merge(p1)
        self.assertIsInstance(p2, Permutation)
        self.assertEqual(p2.slotsGebruikt(), 0)

    def test___merge2__(self):
        p1 = Permutation()
        p1.merge({'key0': 1, 'key1': 2, 'key2': 3})
        p2 = Permutation()
        p2.merge({'key1': 1, 'key2': 2, 'key3': 3})
        p2.merge(p1)
        self.assertIsInstance(p2, Permutation)
        self.assertEqual(p2.slotsGebruikt(), 12)

    def test___sort1__(self):
        p1 = Permutation()
        p1.merge({'key3': 1, 'key1': 2, 'key2': 3})
        keys = []
        for k in p1.keys():
            keys.append(k)
        self.assertEqual(keys[0], 'key3')
        self.assertEqual(keys[1], 'key1')
        self.assertEqual(keys[2], 'key2')
        p1.order()
        keys = []
        for k in p1.keys():
            keys.append(k)
        self.assertEqual(keys[0], 'key1')
        self.assertEqual(keys[1], 'key2')
        self.assertEqual(keys[2], 'key3')

    def test___rank1__(self):
        p1 = Permutation()
        p1.merge({'key3': 1, 'key1': 2, 'key2': 3})
        r = p1.rank()
        self.assertEqual(r, "key31key12key23")

