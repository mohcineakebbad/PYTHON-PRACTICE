class Voiture: 
    # Classe Voiture
    def __init__ (self, marque = "DACIA", modele= "RX-280", année = 2010, kilométrage = 0): 
        # Constructeur de la classe
        self.marque = marque 
        self.modele = modele 
        self.année = année 
        self.kilométrage = kilométrage 

    # Méthode pour faire rouler la voiture
    def rouler(self, km): 
        self.kilométrage += km 
        return self.kilométrage 

    # Méthode pour afficher la description
    def description(self): 
        print(f"marque: {self.marque}\nmodele {self.modele}\n self.année \n kilométrage: {self.kilométrage} ") 

# Classe VoitureElectrique qui hérite de Voiture
class VoitureElectrique(Voiture): 
    # Autonomie initiale
    autonomie = 0 

    # Méthode pour charger la voiture
    def charger(self): 
        self.autonomie = 100

    # Redéfinition de la méthode description
    def description(self): 
            print(f"marque: {self.marque}\nmodele {self.modele}\n self.année \n kilométrage: {self.kilométrage}\nautonomie: {self.autonomie} ") 

# creating objects 
v1 = Voiture() 

# Faire rouler v1 de 10 km
v1.rouler(10) 

# Afficher la description de v1
v1.description() 

# Créer une voiture électrique
v2 =  VoitureElectrique() 

# Faire rouler v2 de 30 km
v2.rouler(30) 

# Charger v2
v2.charger()    

# Afficher la description de v2
v2.description()