class NaZakupy:

    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jd):
        self.x = nazwa_produktu
        self.y = ilosc
        self.z = jednostka_miary
        self.k = cena_jd

    def wyświetl_produkt(self):
        print(self.x,self.y,self.z,self.k)

    def ile_produktu(self):
        print(self.y,self.z)

    def ile_kosztuje(self):
        print(self.y*self.k)

mleko = NaZakupy("Mleko",2,"L",3)
print(mleko.wyświetl_produkt())
print(mleko.ile_produktu())
print(mleko.ile_kosztuje())
