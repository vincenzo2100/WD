import math as m
print('Zadanie 1',m.exp(10))
print('Zadanie 1',m.pow(m.log(5+m.pow(m.sin(8),2)),1/6))
print('Zadanie 1',m.floor(3.55))
print('Zadanie 1',m.ceil(4.80))


imie = 'MICHAŁ'
nazwisko = 'CHOMCZYK'
print('Zadanie 2',imie.capitalize(),nazwisko.capitalize()) 

piosenka = 'la la la bamba' 
print('Zadanie 3',piosenka.count('la'))

print('Zadanie 4',imie[1],imie[5])
lorem = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
print('Zadanie 5',lorem.split())

liczba1 = imie.count(imie[2])
liczba2 = nazwisko.count(nazwisko[2])
print('Zadanie 7','W tekscie jest',liczba1 ,'liter oraz',liczba2 ,'liter')

print('{:>10}'.format('prawo'))
print('{:10}'.format('lewo'))
print('{:_<10}'.format('lewo'))
print('{:^10}'.format('srodek'))
print('{:06.2f}'.format(3.141592653589793))
