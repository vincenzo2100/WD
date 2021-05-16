import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 31, 0.1)
k = np.arange(0,31,0.1)
z = np.sin(k)+2
y = np.sin(x)*(-1)

plt.plot(x,y,label='sin(x)')
plt.plot(k,z,label='sin(x)')
plt.xlim([0,30])
plt.ylim([-1,3])
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.margins(3,3) 
plt.legend()
plt.show()