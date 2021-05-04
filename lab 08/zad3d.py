import pandas as pn  
import csv 
df = pn.read_csv('zamowienia.csv',sep=';',quotechar=';',index_col=None)
y=df.groupby(['Kraj']).agg({'Utarg':['sum']})
print(y)
