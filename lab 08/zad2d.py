import pandas as pn  
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
y=df['Liczba'][(df['Rok']<=2005) & (df['Rok']>=2000)].count()
print(y)