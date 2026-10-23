import numpy as np
A = np.random.rand(15)
print("Avant tri A = ",A)
print("Après tri A= ",np.sort(A))
print("les indices du tri : ",np.argsort(A))