import pandas as pn  
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
cos =df.groupby(['Plec']).count()
print(cos['Liczba'])