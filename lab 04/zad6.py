class Slowa():
    def __init__(self,slowo1,slowo2):
        self.a=slowo1
        self.b=slowo2

    def sprawdz_czy_palindrom(self):
        if self.a == self.a[::-1] and self.b == self.b[::-1]:
            return "Są palindromami"
    
    def sprawdz_czy_metagramy(self):
        if sorted(self.a) == sorted(self.b):
            return "Nie są metagramami"
        else:
            return "Są metagramami"

    def sprawdz_czy_anagramy(self):
        if sorted(self.b) == sorted(self.a):
            return "Są to anagramy"
        else:
           return "Nie są to anagramy"

    def wyswietl_wyraz(self):
        return self.a,self.b

d=Slowa("kajak","tabat")
print(d.sprawdz_czy_palindrom())
print(d.sprawdz_czy_metagramy())
print(d.sprawdz_czy_anagramy())
print(d.wyswietl_wyraz())