from src.Weapon import Weapon

class WeaponsDict:
    def __init__(self, stringFileLocation = ""):
        self.weapons = {}
        with open('../Data/Weapons.csv', 'r') as file:
            print(file.readline())
            rows = file.read().splitlines()
            for row in rows:
                #print(row)
                weapon = Weapon(row)
                self.weapons[weapon.name] = weapon
            print("wapen regels gelezen: ",len(rows))
            print("wapens in dict: ",len(self.weapons))


