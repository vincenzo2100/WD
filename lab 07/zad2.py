import numpy as np
a = np.arange(9).reshape(3,3)
b = np.arange(16).reshape(4,4)
print(a.min(axis=0))
print(a.min(axis=1))
print(a.max(axis=0))
print(a.max(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))
print(b.max(axis=0))
print(b.max(axis=1))

