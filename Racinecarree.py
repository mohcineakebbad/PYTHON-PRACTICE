import math
def racine_carre(nb):
    if nb<0:
        print("entrez un nombre positif")
        return None
    try:
        if nb is None:
            print("Tu as entré rien")
        return math.sqrt(nb)
    except TypeError:
        print("nombre incompatible")
try:
  nb = float(input("veullez entrer un nombre positif"))
  print(racine_carre(nb))
except ValueError:
   print("Type inccorect, veuillez entrer un nombre réel")

