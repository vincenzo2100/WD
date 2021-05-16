import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv',delimiter=';')
sprzedawcy = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
sprzedawcy.plot.pie(subplots=True,autopct='%1.1f%%')
plt.show()