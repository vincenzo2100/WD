class Ciag:
    def __init__(self,a1,r,ilosc):
        self.a1 = a1
        self.r = r
        self.ilosc = ilosc
        
    def wyświetl_dane(self):
        return self.a1,self.r,self.ilosc

    def pobierz_parametry(self):
        return self.a1,self.r,self.ilosc

    def policz_sume(self):
        x = self.a1
        y = self.r
        z = self.ilosc
        return (x+x+(z-1)*y)/2*z

    def policz_elementy(self):
        x = self.a1
        y = self.r
        z = self.ilosc
        an=x+(z-1)*y
        return an

x = Ciag(1,2,10)
print(x.wyświetl_dane())
print(x.pobierz_parametry())
print(x.policz_sume())
print(x.policz_elementy())

