import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
df = pd.read_excel("imiona.xlsx")
grupa = df.groupby(['Plec']).agg({'Imie':['count']})
wykres = grupa.plot.bar()
wykres.legend()
wykres.plot()
plt.title("Liczba urodzonych chłopców i dziewczynek z całego zbioru")
plt.show()
