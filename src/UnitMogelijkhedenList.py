from src.UnitMogelijkheden import UnitMogelijkheden
from src.WeaponsDict import WeaponsDict
from src.UnitMogelijkheden import UnitMogelijkheden

class UnitMogelijkhedenList(list):
    def __init__(self, unitMogelijkhedenFile = "", weaponsFile = ""):
        wd = WeaponsDict(weaponsFile)
        with open(unitMogelijkhedenFile, 'r') as file:
            print(file.readline())
            rows = file.read().splitlines()
            for row in rows:
                print(row)
                unitMogelijkheden = UnitMogelijkheden(row, wd)
                self.append(unitMogelijkheden)
            print("units regels gelezen: ",len(rows))
            print("units in dict: ",len(self))