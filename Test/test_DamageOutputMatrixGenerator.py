from unittest import TestCase

from src.DamageOutputMatrixGenerator import DamageOutputMatrixGenerator
import numpy as np


# Cost; Codex;Unit ;M ;WS ;BS ;S ;T ;W ;A ;Ld ;Save ;Weapons
class TestVariabele(TestCase):

    def test___creation__(self):
        dom = DamageOutputMatrixGenerator(unitMogelijkhedenFile="../Data/Units.csv", weaponsFile="../Data/Weapons.csv")
        self.assertIsInstance(dom, DamageOutputMatrixGenerator)

    def test___creation2__(self):
        dom = DamageOutputMatrixGenerator(unitMogelijkhedenFile="../Data/Units1.csv", weaponsFile="../Data/Weapons1.csv")
        self.assertIsInstance(dom, DamageOutputMatrixGenerator)

    def test___buildList1__(self):
        dom = DamageOutputMatrixGenerator(unitMogelijkhedenFile="../Data/Units.csv", weaponsFile="../Data/Weapons.csv")
        bl = dom.simpelMatrix()
        self.assertIsInstance(bl, np.ndarray)

    def test___buildList2__(self):
        dom = DamageOutputMatrixGenerator(unitMogelijkhedenFile="../Data/Units1.csv", weaponsFile="../Data/Weapons1.csv")
        bl = dom.simpelMatrix()
        self.assertIsInstance(bl, np.ndarray)
