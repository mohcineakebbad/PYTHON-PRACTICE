def acess(dicte, key):
    print(dicte[key])
    print(dicte)
#main
dict1 = {"voiture":"renault","year":2027}
cle = input("veuillez tapper un clé")
try:
 if cle not in dict1:
    print("le clé n'existe pas ")
 acess(dict1, cle)
except KeyError:
   print("le clé est inexistant ")
except TypeError:
   print("type de clé incompatible")

