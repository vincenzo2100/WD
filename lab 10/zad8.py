import pandas as pd
import matplotlib.pyplot as plt
import random
def rzucaj(n):
    random.seed()
    ile=0
    lista = []
    while ile<=n:
        z = random.randint(1, 6)
        y = random.randint(1, 6)
        lista.append(z+y)
        ile+=1
    return lista

x = rzucaj(5)
plt.hist(x)
plt.xlabel('Suma rzutu')
plt.show()