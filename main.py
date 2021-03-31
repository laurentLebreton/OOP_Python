from animal import *
from serpent import *
from oiseau import *
from zoo import *


monAnimal = Animal(100,180)
monAnimal2 = Animal(2100,2180)
#print ("poids :" + str(monAnimal.get_poids()))
#print ("taille :" + str(monAnimal.get_taille()))

monAnimal.set_poids(100)

#print(dir(monAnimal))

monSerpent= Serpent(10,20)
monSerpent2= Serpent(210,220)
#monSerpent.se_deplacer()

monOiseau= Oiseau(50,30,100)
monOiseau2= Oiseau(250,230,2100)
#monOiseau.se_deplacer()

monZoo = Zoo(monAnimal,monSerpent,monOiseau)
monZoo2 = Zoo(monAnimal2,monSerpent2,monOiseau2)

monNouveauZoo = monZoo + monZoo2

print(monNouveauZoo[4].get_taille())

#print(monZoo.animaux[1].get_taille())