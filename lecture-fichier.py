def readfile(filename):
    try:
        f1=open(filename, "r", encoding="UTF-8")
        c=f1.read()
        f1.close()
        if c == "":
          raise ValueError("fichier vide")
        return c
    except FileNotFoundError:
     print("veuillez entrer un nom d'un fichier qui existe")
    except PermissionError:
     print("permission refusé")
    except ValueError as e:
     print("Erreur :", e)
    
f2=open("New file", "w", encoding="UTF-8")
f2.write("You can do it")
f2.close()
f3=open("New file (2)", "w", encoding="UTF-8")
f3.close()
filename = input("saisez le nom du fichier ")
print(readfile(filename))

