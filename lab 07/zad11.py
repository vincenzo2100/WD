import numpy as np
a = np.arange(12)
b = a.ravel()
c = b.reshape(3,4)
d = b.reshape(4,3)
e = b.reshape(2,6)
print(c)
print(d)
print(e)
