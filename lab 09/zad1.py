import pandas as pd 
import matplotlib.pyplot as plt
import xlrd
import openpyxl
df = pd.read_excel("imiona.xlsx")
grupa = df.groupby(['Rok']).agg({'Imie':['count']})
wykres = grupa.plot()
wykres.set_xlabel("Rok")
wykres.legend()
wykres.plot()
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()
