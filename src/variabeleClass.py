# used to have flexibility in the way we operate with variabeles
import re

class Variabele:
    def __init__(self, stringIn=""):
        #check format
        match = re.match("^[0-9]?d?[0-9][0-9]?$", stringIn)
        if not match:
            raise ValueError("it's not a constant or a die")

        if stringIn[0] == "d":
            stringIn = stringIn[1:]
            self.waarde = list(range(int(stringIn)))
        elif stringIn[1] != "d":
            self.waarde = list(range(int(stringIn), int(stringIn)))
        else



            #if eersteletter d
        # dan dice
        #anders vaste waarde

    def kansdichtheid(self, dobbelsteen, aantal):
        kdl = {}
        for i in range(dobbelsteen):
            kdl[i] = 1 / dobbelsteen
        if aantal == 1:
            kd = kdl
        else:
            kd = {}
            for k in kansdichtheid(dobbelsteen, aantal - 1):
                for kl in kdl:
                    x=1


