import numpy as np
X = np.random.rand(100, 1)
y = 3*X[:, 0]+2+np.random.randn(100) # exemple 
print("X = ", X)
print("y = ", y)