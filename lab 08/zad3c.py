import pandas as pn  
import csv 
df = pn.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
y=df.groupby(['Sprzedawca']).agg({'Sprzedawca':['count']})
print(y)
