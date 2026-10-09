def conversion(L):
    L=list(map(int, L))
    return L
M=list(input("veuillez saiser des élement de la liste"))
try:
 if M=="":
     print("la liste est vide ")
 print(conversion(M))
except ValueError:
   print("éléments non convertible")
   

