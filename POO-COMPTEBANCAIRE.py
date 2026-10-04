class  CompteBancaire:
    def __init__(self, nbcompte = 0, nom = "", solde = 0):
        self.nbcompte = nbcompte
        self.nom = nom
        self.solde = solde
    def deposer (self):
         montant=int(input("tappez la somme que vous voulez déposer"))
         self.solde += montant
         if self.solde>0 :
              print("Votre montant est désposée en succés")
         else:
              print("montant ivalide")
    
         
    def retirer(self):
         r=int(input("tappez la somme que vous voulez tirer"))
         if r>self.solde:
              print("votre solde est insuffisant")
         elif r<0:
              print("solde invalide ")          
         else:
              self.solde-=r
              print("Prenez votre argent")
    def afficher(self):
         print(f"le solde est {self.solde}")
              
client1 = CompteBancaire()
client1.nom = input("Tappez votre nom ")
client1.nbcompte = 130188575
client1.afficher()
client1.deposer()
client1.retirer()
client1.afficher()