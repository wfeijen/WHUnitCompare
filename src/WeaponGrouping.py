import re

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





