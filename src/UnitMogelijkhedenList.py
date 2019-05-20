from src.UnitMogelijkheden import UnitMogelijkheden
from src.WeaponsDict import WeaponsDict

class UnitMogelijkhedenList(list):
    def __init__(self, unitMogelijkhedenFile = "", weaponsFile = ""):
        wd = WeaponsDict(weaponsFile)
        with open('../Data/Weapons.csv', 'r') as file:
            print(file.readline())
            rows = file.read().splitlines()
            for row in rows:
                #print(row)
                weapon = Weapon(row)
                self.weapons[weapon.name] = weapon
            print("wapen regels gelezen: ",len(rows))
            print("wapens in dict: ",len(self.weapons))