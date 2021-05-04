import pandas as pd
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
print(df.groupby(['Rok']).agg({'Imie':['count']}))
print(df[df['Imie']=='MICHAŁ'])
print(df.agg({'Imie':['count']}))
##brakuje
print(df.groupby(['Plec']).agg({'Imie':['count']}))
print(df.groupby(['Imie']).agg({'Imie':['count']}))