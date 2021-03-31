from animal import *

class Oiseau(Animal):
    def __init__(self, poids, taille,altitudeVol):
        super().__init__(poids, taille)
        self.__altitudeVol = altitudeVol

    def se_deplacer(self):
        print("je vole")

    def get_altitudeVol(self):
        return self.__altitudeVol

    def set_altitudeVol(self,paltitudeVol):
        self.__altitudeVol = altitudeVol