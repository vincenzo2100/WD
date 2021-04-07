class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __eq__(self, y):
        if self.x ==y.x:
            return " sa rowne"
        else:
            return "nie sa rowne"

    def __lt__(self, y):
        if self.x<y.x:
            return "pierwszy mniejszy"
        else:
            return "pierwszy nie mniejszy"

    def __gt__(self, y):
        if self.x>y.x:
            return "pierwszy  wiekszy"
        else:
            return "pierwszy   nie wiekszy "
    def __ge__(self,y):
        if self.x>=y.x:
            return "pierwszy wiekszy rowny"
        else:
            return "pierwszy nie wiekszy rowny"
    def __le__(self,y):
        if self.x<=y.x:
            return "pierwszy mniejszy lub rowny"
        else:
            return " pierwszy nie mniejszy lub rowny"
print("inicjujemy klasę Kwadrat")
figura = Kwadrat(5)
figa= Kwadrat(10)
print(figa<figura)
print(figura==figa)
print(figura>figa)
print(figura>=figa)
print(figa>=figura)
print(figa<=figura)
 

