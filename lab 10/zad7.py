import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
m = df[(df.Plec == 'M')].groupby('Rok').agg({'Imie':['count']})
k = df[(df.Plec == 'K')].groupby('Rok').agg({'Imie':['count']})
fig, ax = plt.subplots()

ax.bar(df['Rok'], m, 0.35, yerr=m, label='Men')
ax.bar(df['Rok'], k, 0.35, yerr=k, bottom=m,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()