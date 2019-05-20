import numpy as np

import csv

file = open('../Data/Weapons.csv', 'r')

print(file.readline())

file.close()

class Artest(list):
    def __init__(self, i, ar):
        self.x = i
        self.extend(ar)

a = Artest(1, [4,2,3])

print(a.x)

#a.append(5)

print(a[0])