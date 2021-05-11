import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
grupa = df.groupby(['Plec']).agg({'Imie':['count']})
z = grupa.iloc[-5:]
wykres = z.plot.pie(subplots=True,autopct='%.2f %%')
plt.title("Ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu")
plt.show()
