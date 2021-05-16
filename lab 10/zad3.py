import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 31, 0.1)
z = np.sin(x)
y = np.cos(x)

plt.plot(x,z,label='Wykres sin(x)')
plt.plot(x,y,label='Wykres cos(x)')
plt.legend()
plt.show()