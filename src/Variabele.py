# used to have flexibility in the way we operate with variabeles
import re


def waardenVerdeling(dobbelsteen, aantal):
    waardenDitLevel = list(range(1, dobbelsteen + 1))
    if aantal == 1:
        waarden = waardenDitLevel
    else:
        waarden = []
        for waardeVolgendLevel in waardenVerdeling(dobbelsteen, aantal - 1):
            for waardeDitLevel in waardenDitLevel:
                waarden.append(waardeVolgendLevel + waardeDitLevel)
    return waarden


class Variabele:
    def __init__(self, stringIn=""):
        if re.match("^[0-9][0-9]?$", stringIn):
            self.waarde = [int(stringIn)]
        elif re.match("^d[0-9][0-9]?$", stringIn):
            stringIn = stringIn[1:]
            self.waarde = waardenVerdeling(int(stringIn), 1)
        elif re.match("^[0-9]d[0-9][0-9]?$", stringIn):
            nrs = list(map(int, stringIn.split("d")))
            self.waarde = waardenVerdeling(nrs[1], nrs[0])
        else:
            raise ValueError(stringIn, " it's not a constant or a die")




