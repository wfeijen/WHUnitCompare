class ModelBuild:
    def __init__(self, modelEigenschappen, weaponBuild):
        self.modelEigenschappen = modelEigenschappen
        self.weaponBuild = weaponBuild
        self.cost = self.modelEigenschappen.cost
        #for weapon, number in weaponBuild.items():
        #    self.cost += weapon.cost * number
