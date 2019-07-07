from collections import defaultdict

class Permutation(defaultdict):
    def __init__(self):
        super(Permutation, self).__init__(int)
        self.gedoken = False

    @classmethod
    def createWithOneElement(self, object, ammount):
        dummy = Permutation()
        dummy[object] = ammount
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
                dummy[weapon] += aantal
                permutatiesUit.append(dummy)
        return permutatiesUit

    def order(self):
        items = sorted(self.items())
        self.clear()
        for k,v in items:
            self[k] = v

    def rank(self):
        r = ""
        for k, v in self.items():
            r += k.name + str(v)
        return r