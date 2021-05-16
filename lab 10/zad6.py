import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
grupa = df.groupby(['Plec']).agg({'Imie':['count']})
m = df[(df.Plec == 'M')].groupby('Rok').agg({'Imie':['count']})
k = df[(df.Plec == 'K')].groupby('Rok').agg({'Imie':['count']})
suma = df.groupby(['Rok']).agg({'Liczba':['sum']})
figure, axes = plt.subplots(1, 3)
grupa.plot(ax=axes[0],kind='bar')
plt.plot(m)
plt.plot(k)
suma.plot(ax=axes[1],kind='bar')
plt.show()