class Animal:
    def __init__(self, poids, taille):
        self.__poids = poids
        self.__taille = taille

    def get_poids(self):
        return self.__poids

    def get_taille(self):
        return self.__taille

    def set_poids(self,poids):
        try:
            if poids < 0 :
                raise ValueError
            self.__poids = poids
        except ValueError :
            print("La valeur passée en paramétre doit être un entier positif")

    def set_taille(self,taille):
        self.__taille = taille
    
    def se_deplacer():
        pass

    def __str__(self):
        return ("l'animal pése :" + str(self.__poids) + " kg et mesure : " +str(self.__taille) + " cm")
       


