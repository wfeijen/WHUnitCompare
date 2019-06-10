from collections import defaultdict

class Permutation(defaultdict):
    def __init__(self):
        super(Permutation, self).__init__(int)
        self.gedoken = False

    @classmethod
    def createWithOneElement(self, name, ammount):
        dummy = Permutation()
        dummy[name] = ammount
        return dummy

    def slotsGebruikt(self):
        return sum(self.values())

    def merge(self, newDict):
        for k, v in newDict.items():
            self[k] += v

    def copy(self):
        newPermutatie = Permutation()
        newPermutatie.merge(self)
        return newPermutatie

    def combineToNewPermutationsWithWeapons(self, aantal, weapons):
        permutatiesUit = list()
        if aantal <= 0: return list()
        else:
            for weapon in weapons:
                dummy = self.copy()
                dummy[weapon.name] += aantal
                permutatiesUit.append(dummy)
        return permutatiesUit