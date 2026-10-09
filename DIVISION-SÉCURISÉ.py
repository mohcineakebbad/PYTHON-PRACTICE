a=float(input("veuillez tapper le numérateur"))
b=float(input("veuiller determiner le dénominateur"))
try:
    print("la division est: ",a/b)
except TypeError:
    print("veuillez entrer des nombres réels ")
except ZeroDivisionError:
    print("entrez un dénominateur différent à zero")

    
