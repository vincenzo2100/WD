import pandas as pd
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
x = df.groupby(['Rok']).agg({'Imie':['count']})
z = x.nlargest(2,x)
print(z)