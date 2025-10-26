def estpairF(a):
    if a%2==0:
        return 1
    else:
        return 0
def estpairP(a):
    if estpairF(a)==1:
       print("ce nombre est pair")
    else:
        print("ce nombre est impair")
n=int(input("saisez un entier:"))
estpairF(n)
estpairP(n)


