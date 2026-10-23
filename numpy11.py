import numpy as np
A = np.array([1, np.nan, 3])
print(A)
print("le moyen de A = ",np.nanmean(A))