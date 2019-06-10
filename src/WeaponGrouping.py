import re
from src.Weapon import Weapon
from src.Permutation import Permutation


#1|A
#1-6|A,B
#1-6|A,B[0-4|C,D]
#1-6|A,B[0-4|C,[0-4|E,F][0-4|D]]
#1-6|[0-3|A,B][0-3|C,D][0-3|E,F]

class WeaponGrouping:
    def __init__(self, stringIn, weaponDictionary):
        # Aanmaken lijsten
        self.weapons = list()
        self.weaponGroupings = list()
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
                self.weapons.append(weapon)
                weaponName = ""
            elif groupContents[i] == "[":
                if haakjesDiepte == 0:
                    groepString = ""
                    if weaponName != "":
                        weapon = weaponDictionary[weaponName]
                        self.weapons.append(weapon)
                        weaponName = ""
                else:
                    groepString = groepString + groupContents[i]
                haakjesDiepte = haakjesDiepte + 1
            elif groupContents[i] == "]":
                haakjesDiepte = haakjesDiepte - 1
                if haakjesDiepte == 0:
                    nieuweWeaponGroup = WeaponGrouping(groepString, weaponDictionary)
                    self.weaponGroupings.append(nieuweWeaponGroup)
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
            self.weapons.append(weapon)

    def combineerMetPermutatiesZelfdeLevel(self, weaponsSlotsToUseMin, weaponsSlotsToUseMax, counter, permutatieList):
        permutationsReturn = []
        for permutatieDL in permutatieList:
            permutatiesZelfdeLevel = self.permutationsOfGroupsInSameLevel(weaponsSlotsToUseMin - permutatieDL.slotsGebruikt(),
                                                                          weaponsSlotsToUseMax - permutatieDL.slotsGebruikt(),
                                                                          counter)

            for permutatieZL in permutatiesZelfdeLevel:
                permutatie = permutatieDL.copy()
                permutatie.merge(permutatieZL)
                permutationsReturn.append(permutatie)
            permutationsReturn.append(permutatieDL)
        return permutationsReturn

    def permutationsOfGroupsInSameLevel(self, weaponsSlotsToUseMin, weaponsSlotsToUseMax, counter):
        # Checkt op min en max en besteedt zoeken naar permutaties met maximale en minimale vulling voor dit slot uit

        # Ontsnappingsclausules
        if counter == len(self.weaponGroupings): return ([])  # er is maar 1 mogelijkheid
        if weaponsSlotsToUseMax == 0: return ([])  # er is maar 1 mogelijkheid
        if weaponsSlotsToUseMax < weaponsSlotsToUseMin:
            return ([])  # niet valide, dus we geven geen permutaties terug

        permutationsReturn = []
        # we proberen eerst te duiken voor deze slot en kijken of andere slots op dit level aan de condities kunnen voldoen
        if weaponsSlotsToUseMin == 0 or counter < len(self.weaponGroupings) + len(self.weapons) - 1:
            gevondenPermutaties = self.permutationsOfGroupsInSameLevel(weaponsSlotsToUseMin, weaponsSlotsToUseMax, counter + 1)
            permutationsReturn.extend(gevondenPermutaties)
        # wat als we zorgen dat we voldoen aan minOccurences door nu die minoccurences te pakken of in ieder geval voor de max proberen te gaan
        if weaponsSlotsToUseMin > 0:
            gevondenPermutatiesDieperLevel = self.weaponGroupings[counter].permutatiesNewLevel(0, weaponsSlotsToUseMin)
            for permutatie in gevondenPermutatiesDieperLevel: permutatie.gedoken = True
            permutationsReturn.extend(gevondenPermutatiesDieperLevel)

        # max out on this weapon
        if weaponsSlotsToUseMin < weaponsSlotsToUseMax:  # anders gelijk aan min
            gevondenPermutatiesDieperLevel = self.weaponGroupings[counter].permutatiesNewLevel(weaponsSlotsToUseMin, weaponsSlotsToUseMax)
            #verwijderen gedoken permutaties
            gevondenPermutatiesDieperLevel = [p for p in gevondenPermutatiesDieperLevel if p.gedoken == False]
            permutationsReturn.extend(self.combineerMetPermutatiesZelfdeLevel(weaponsSlotsToUseMin,
                                                                         weaponsSlotsToUseMax,
                                                                         counter + 1, gevondenPermutatiesDieperLevel))
        return permutationsReturn

    def permutatiesNewLevel(self, weaponsSlotsToUseMinIn, weaponsSlotsToUseMaxIn):
        # retourneert een lijst met permutaties (lijst met lijsten)
        # we zoeken eerst permutaties van onderliggende weapon groepen
        # vervolgens maxen en minnen we uit met losse weapons in deze groep,
        # In dat geval is telkens 1 wapen optimaal, dus dat hoeft niet recursief.
        # Elke wapen wordt gecombineerd in een max en een min variant.

        # Preposities:
        # Elke groep min en max is kleiner of gelijk aan die van de omvattende groep
        # Groeps max binnen omvattende groep zijn opklimmend

        # Creeren nieuwe min en max op basis van input en locale min en max
        weaponsSlotsToUseMin = max(weaponsSlotsToUseMinIn, self.minOccurences)
        weaponsSlotsToUseMax = min(weaponsSlotsToUseMaxIn, self.maxOccurrences)

        # Checks of dit level aan de eisen kan voldoen qua min en max
        if weaponsSlotsToUseMax < weaponsSlotsToUseMin: return [] # niet valide, dus we geven geen permutaties terug
        if weaponsSlotsToUseMax == 0: return ([Permutation()]) # er is maar 1 mogelijkheid

        permutationsInMyGoups = self.permutationsOfGroupsInSameLevel(weaponsSlotsToUseMin, weaponsSlotsToUseMax, 0)
        permutationsReturn = []
        for permutationInMyGroup in permutationsInMyGoups:
            if len(permutationInMyGroup) > 0:
                minLosseWeapons = max(0, weaponsSlotsToUseMin - permutationInMyGroup.slotsGebruikt())
                if minLosseWeapons == 0:  # Er hoeven geen losse wapens toegevoegd te worden.
                    permutationsReturn.append(permutationInMyGroup)
                if permutationInMyGroup.gedoken == False:
                    permutationsReturn.extend(permutationInMyGroup.combineToNewPermutationsWithWeapons(minLosseWeapons, self.weapons))
                    maxLosseWeapons = weaponsSlotsToUseMax - permutationInMyGroup.slotsGebruikt()
                    if maxLosseWeapons > 0:
                        permutationsReturn.extend(permutationInMyGroup.combineToNewPermutationsWithWeapons(maxLosseWeapons, self.weapons))
        if weaponsSlotsToUseMax >0:
            for weapon in self.weapons:
                permutationsReturn.append(Permutation.createWithOneElement(weapon.name, weaponsSlotsToUseMax))
                if weaponsSlotsToUseMin > 0 and weaponsSlotsToUseMin < weaponsSlotsToUseMax:
                    permutation = Permutation.createWithOneElement(weapon.name, weaponsSlotsToUseMin)
                    permutation.gedoken = True
                    permutationsReturn.append(permutation)
        return permutationsReturn







