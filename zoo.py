from animal import *

class Zoo():
    def __init__(self,*args):
        self.animaux = []
        for i in args :
            self.animaux.append(i)

    def ajouter_animal(self,animal):
        self.aninaux.append(animal)

    def __add__(self, other):
        self.animaux += other.animaux
        return self.animaux