import numpy as np
def funkcja(n):
    macierz=np.zeros((n,n))
    i=0
    for x in range (n):
        for j in range(n):
            macierz[x][j]=i
            i+=1
    return macierz
print(funkcja(7))