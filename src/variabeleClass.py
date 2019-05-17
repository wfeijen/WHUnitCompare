# used to have flexibility in the way we operate with variabeles
import re

class Variabele:
    def __init__(self, stringIn=""):
        #check format
        match = re.match("^d?[0-9][0-9]?$", stringIn)
        if not match:
            raise ValueError("it's not a constant or a die")

            #if eersteletter d
        # dan dice
        #anders vaste waarde
