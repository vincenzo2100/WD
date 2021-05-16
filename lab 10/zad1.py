import matplotlib.pyplot as plt
import pandas as pn 
import numpy as np

x = np.linspace(1, 20,20)

plt.plot(x, 1/x, label='1/x')

plt.title('Wykres funkcji f(x) dla x[1,20]')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
