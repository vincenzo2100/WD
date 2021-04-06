class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc,rozmiar,kolor,dla_kogo):
        self.r = rodzaj
        self.d = dlugosc
        self.s = szerokosc
        self.ro = rozmiar
        self.k = kolor
        self.dk = dla_kogo


    def wyswietl_nazwe(self):
        return self.r,self.d,self.s

class Ubrania(Material):

    def wyswietl_dane(self):
        return self.ro,self.k,self.dk

class Swetry(Ubrania):
    def wyswietl_dane(self):
        return self.r,self.d,self.s,self.ro,self.k,self.dk


pom = Swetry("bawełna",2,3,"L","czarny","Seba")
print(pom.wyswietl_dane())

    