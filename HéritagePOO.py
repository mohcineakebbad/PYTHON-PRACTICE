class Personne:
    def __init__ (self, nom = "", prenom = "", age = 0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
class Etudiant(Personne):
    def __init__ (self, numero = 0, filiere = "", moyenne= 0):
        self.numero = numero
        self.filiere = filiere
        self.moyenne = moyenne
    def est_admis(self):
        if self.moyenne>=10:
           return True
        else:
            return False
E1=Etudiant()
E1.nom = "AKEBBAD"
E1.prenom = "MOHCINE"
E1.age = 20
E1.numero = 25
E1.filiere = "MGSI"
E1.moyenne = 16
print(f"{E1.nom} {E1.prenom} qui a {E1.age} de numéro {E1.numero} a obtenu {E1.moyenne}")
print(f"Admis? : {E1.est_admis()}")
