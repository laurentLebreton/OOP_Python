from animal import *

class Zoo():
    def __init__(self,liste):
        self.animaux = []
        for i in liste :
            self.animaux.append(i)

    def ajouter_animal(self,animal):
        self.animaux.append(animal)

    def __add__(self, other):
        newZoo = Zoo(self.animaux + other.animaux) 
        return newZoo

    def get_taille(self):
        return len(self.animaux)