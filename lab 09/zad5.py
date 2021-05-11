import pandas as pd 
import matplotlib.pyplot as plt
import csv 
df = pd.read_csv('zamowienia.csv',sep=";",quotechar=';')
grupa = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = grupa.plot.bar()  
plt.title("Ilość złożonych zamówień przez poszczególnych sprzedawców")
plt.show()