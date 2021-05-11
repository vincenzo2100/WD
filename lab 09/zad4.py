import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.data",sep=',')
x = df['Dlugosc_kielicha'][(df['Gatunek']=='Iris-setosa')]
y = df['Szerokosc_kielicha'][(df['Gatunek']=='Iris-setosa')]
plt.scatter(x,y,color='red',label='Iris-setosa')
x = df['Dlugosc_kielicha'][(df['Gatunek']=='Iris-versicolor')]
y = df['Szerokosc_kielicha'][(df['Gatunek']=='Iris-versicolor')]
plt.scatter(x,y,color='blue',label='Iris-versicolor')
x = df['Dlugosc_kielicha'][(df['Gatunek']=='Iris-virginica')]
y = df['Szerokosc_kielicha'][(df['Gatunek']=='Iris-virginica')]
plt.scatter(x,y,color='green',label='Iris-virginica')
plt.legend()
plt.xlabel("Długość kielicha")
plt.ylabel("Szerokość kielicha")
plt.title("Porównanie długości i szerokości kielichów")
plt.show()