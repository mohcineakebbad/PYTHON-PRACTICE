import numpy as np
A = np.random.randint(-10, 11, 10)
print("Tableau initial :", A)
mask = A<0
A[mask]=0
print("Tableau modifié :", A)