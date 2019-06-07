from collections import defaultdict

class Permutatie(defaultdict):
    def __init__(self):
        super(Permutatie, self).__init__(int)

    def slotsGebruikt(self):
        return sum(self.values())

    def merge(self, newDict):
        for k, v in newDict.items():
            self[k] += v

    def copy(self):
        newPermutatie = Permutatie()
        newPermutatie.merge(self)
        return newPermutatie