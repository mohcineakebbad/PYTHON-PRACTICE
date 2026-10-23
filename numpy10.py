import numpy as np
A = np.eye(5,3)
print("A = ",A)
print("la somme par colonne = ",np.sum(A, axis = 0))
print("le moyen entre les ligne = ",np.mean(A, axis = 1))