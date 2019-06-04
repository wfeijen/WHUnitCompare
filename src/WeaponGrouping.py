import re
from src.Weapon import Weapon
from src.Permutatie import Permutatie


#1|A
#1-6|A,B
#1-6|A,B[0-4|C,D]
#1-6|A,B[0-4|C,[0-4|E,F][0-4|D]]
#1-6|[0-3|A,B][0-3|C,D][0-3|E,F]

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

    def permutaties(self, weaponSlotsUsed, weaponsSlotsToUse, counter):
        # retourneert een lijst met permutaties (lijst met lijsten) en een lijst met slotsOver

        # Ontsnappingsclausules
        if counter == len(self): return ([Permutatie()])
        if weaponsSlotsToUse == 0: return ([Permutatie()])
        maxUse = min(weaponsSlotsToUse, self.maxOccurrences)
        minUse = max(0, self.minOccurences - weaponSlotsUsed)
        if maxUse < minUse: return None

        # for weapon in Counter we either take none, all or whats left, then we do a new iteration with counter +1
        permutatiesTerug = [] # list of dictionaries met wapen-naam, aantal

        # Twee permutaties
        # minimalizeer het aantal van dit wapen
        if self.minOccurences > maxUse: return None

        if type(self[counter]) ==  Weapon:
            # minimize use of this weapon Dit kan op twee manieren. O pakken en andere in dezelfde groep de min laten pakken of min pakken
            # kijken of we de min door kunnen schuiven naar een ander en zo ja pak 0
            if minUse == 0 or counter < len(self) - 1:
                gevondenPermutaties = self.permutaties(weaponSlotsUsed, weaponsSlotsToUse , counter + 1)
                if type(gevondenPermutaties) == list: #Kan denk ik weg
                    permutatiesTerug.extend(gevondenPermutaties)
            # wat als we zorgen dat we voldoen aan minOccurences door nu die occurences te pakken
            if minUse > 0:
                gevondenPermutatie = Permutatie() # we hoeven niet echt meer een aanroep te doen want een ander kan al geen maxuse meer doen
                gevondenPermutatie[self[counter].name] += minUse
                permutatiesTerug.append(gevondenPermutatie)
            # max out on this weapon
            if minUse < maxUse: # anders gelijk aan min
                gevondenPermutatie = Permutatie() # we hoeven niet echt meer een aanroep te doen want alles is opgebruikt
                gevondenPermutatie[self[counter].name] += maxUse
                permutatiesTerug.append(gevondenPermutatie)
        else: # Not a weapon
            # minimize use of this weapon Dit kan op twee manieren. O pakken en andere in dezelfde groep de min laten pakken of min pakken
            # kijken of we de min door kunnen schuiven naar een ander en zo ja pak 0
            if minUse == 0 or counter < len(self) - 1:
                gevondenPermutaties = self.permutaties(weaponSlotsUsed, weaponsSlotsToUse , counter + 1)
                if type(gevondenPermutaties) == list: #Kan denk ik weg
                    permutatiesTerug.extend(gevondenPermutaties)
            # wat als we zorgen dat we voldoen aan minOccurences door nu die occurences te pakken
            if minUse > 0:
                gevondenPermutatiesDieperLevel = self[counter].permutaties(0, minUse, 0)
                if type(gevondenPermutatiesDieperLevel) == list: #Kan denk ik weg
                    for permutatieDL in gevondenPermutatiesDieperLevel:
                        if permutatieDL.slotsGebruikt() < minUse and counter < len(self) -1:
                            permutatiesZelfdeLevel = self.permutaties(weaponSlotsUsed + permutatieDL.slotsGebruikt(),
                                                                      weaponsSlotsToUse - permutatieDL.slotsGebruikt() ,
                                                                      counter + 1)
                            for permutatieZL in permutatiesZelfdeLevel:
                                permutatie = permutatieDL
                                permutatie.merge(permutatieZL)
                                permutatiesTerug.append()
                    permutatiesTerug.extend(gevondenPermutaties)
            # max out on this weapon
            if minUse < maxUse: # anders gelijk aan min
                gevondenPermutatie = Permutatie() # we hoeven niet echt meer een aanroep te doen want alles is opgebruikt
                gevondenPermutatie[self[counter].name] += maxUse
                permutatiesTerug.append(gevondenPermutatie)
        return permutatiesTerug







