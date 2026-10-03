class Personne:
    nom = ""
    prenom = ""
    age = 0
    def afficher (self):
        print(f"nom{self.nom}\nprenom{self.prenom}\nage:{self.age}")
    def modifier(self, age):
        self.age = age
    def verification(self):
        if self.age>=18 :
            print("cette personne est majeur")
        else:
            print("cette personne est mineur")
p1 = Personne()
p1.nom = "AKEBBAD"
p1.prenom = "MOHCINE"
p1.age = 20
p2 = Personne()
p2.nom = "OUSSAMA"
p2.prenom = "kouti"
p2.age = 16
p1.afficher()
p1.verification()
p2.afficher()
p2.verification()
p2.modifier(18)
p2.verification()
p2.afficher()



    