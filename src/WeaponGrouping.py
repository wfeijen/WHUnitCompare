import re
from src.Weapon import Weapon

#1|A
#1-6|A,B
#1-6|A,B[0-4|C,D]
#1-6|A,B[0-4|C,[0-4|E,F][0-4|D]]
#1-6|[0-3|A,B][0-3|C,D][0-3|E,F]

from collections import defaultdict

class WeaponGrouping(list):
    def __init__(self, stringIn, weaponDictionary):
        # Schonen string
        geschoondeString = re.sub(' *, *', ',', stringIn)
        # left from | is the possible occurrences
        possibleOccurencesString = re.match("[0-9\-]+[\|*]", geschoondeString).group(0)
        possibleOccurences = possibleOccurencesString[:-1].split("-")
        if possibleOccurencesString[-1:] == "|":
            self.minOccurences = int(possibleOccurences[0])
            self.wapensInSlot = 1
            if (len(possibleOccurences)>1):
                self.maxOccurrences = int(possibleOccurences[1])
            else:
                self.maxOccurrences = self.minOccurences
        else:
            self.minOccurences = 0
            self.maxOccurrences = 100
            self.wapensInSlot = int(possibleOccurences[0])

        if self.minOccurences > self.maxOccurrences:
            print("############")
            print("     De volgende wapengroeperingsregel gaat tot problemen leiden: ", stringIn)
            print("     Minimunaantal groter dan maximumaantal.")

        groupContents = geschoondeString[len(possibleOccurencesString):]
        weaponName = ""
        haakjesDiepte = 0
        for i in range(len(groupContents)):
            if groupContents[i] == "," and haakjesDiepte == 0:
                weapon = weaponDictionary[weaponName]
                self.append(weapon)
                weaponName = ""
            elif groupContents[i] == "[":
                if haakjesDiepte == 0:
                    groepString = ""
                    if weaponName != "":
                        weapon = weaponDictionary[weaponName]
                        self.append(weapon)
                        weaponName = ""
                else:
                    groepString = groepString + groupContents[i]
                haakjesDiepte = haakjesDiepte + 1
            elif groupContents[i] == "]":
                haakjesDiepte = haakjesDiepte - 1
                if haakjesDiepte == 0:
                    nieuweWeaponGroup = WeaponGrouping(groepString, weaponDictionary)
                    self.append(nieuweWeaponGroup)
                else:
                    groepString = groepString + groupContents[i]
            elif haakjesDiepte == 0:
                weaponName = weaponName + groupContents[i]
            else:
                groepString = groepString + groupContents[i]
        if weaponName != "":
            try:
                weapon = weaponDictionary[weaponName]
            except KeyError as e:
                print("############")
                print("     De volgende wapengroeperingsregel kon niet verwerkt worden: ", stringIn)
                print("     Wapen:", weaponName, " kon niet gevonden worden in de dictionary")
                print("     De foutmelding is:", e.args)
            self.append(weapon)
        self.sort(key = lambda x: x.maxOccurrences, reverse=False)

    def permutaties(self, weaponsSlotsToUse, counter):
        # retourneert een lijst met permutaties (lijst met lijsten) en een lijst met slotsOver

        # Ontsnappingsclausules
        if counter == len(self): return ([defaultdict(int)])
        if weaponsSlotsToUse == 0: return ([defaultdict(int)])

        # for weapon in Counter we either take none, all or whats left, then we do a new iteration with counter +1
        permutatiesTerug = [] # list of dictionaries met wapen-naam, aantal
        if type(self[counter]) ==  Weapon:
            # Twee permutaties
            # minimalizeer het aantal van dit wapen
            if self.minOccurences > weaponsSlotsToUse: return None

            # minimize use of this weapon
            permnutatiesMin = self.permutaties(weaponsSlotsToUse - self.minOccurences, counter + 1)
            if type(permnutatiesMin) == list:
                for permutatie in permnutatiesMin:
                    permutatie[self[counter].name] += self.minOccurences
                permutatiesTerug.extend(permnutatiesMin)
            # max out on this weapon
            maxUse = min(weaponsSlotsToUse, self.maxOccurrences)
            if self.minOccurences < maxUse: # anders gelijk aan min
                permnutatiesMax = self.permutaties(weaponsSlotsToUse - maxUse, counter + 1)
                if type(permnutatiesMax) == list:
                    for permutatie in permnutatiesMax:
                        permutatie[self[counter].name] += maxUse
                    permutatiesTerug.extend(permnutatiesMax)

        return permutatiesTerug







