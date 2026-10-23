import numpy as np
m = np.random.randint(0, 101, 20)
print(m)
mask = m>50
print(mask)
result = m[mask]
print(result)