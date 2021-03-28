class Robot:
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.z = krok

    def idz_w_gore(self):
        self.y += self.z
        return self.x,self.y

    def idz_w_dol(self):
        self.y -= self.z
        return self.x,self.y 

    def idz_w_lewo(self):
        self.x -= self.z
        return self.x,self.y
    
    def idz_w_prawo(self):
        self.x += self.z
        return self.x,self.y

    def pokaz_gdzie_jestes(self):
        return self.x,self.y
        
    def __del__(self): 
        print("Niszczenie" + str(self.x) + str(self.y) + str(self.z) )

    

r = Robot(0,0,5)
r.idz_w_gore()
r.idz_w_gore()
r.idz_w_gore()
r.idz_w_dol()
r.idz_w_dol()
r.idz_w_lewo()
r.idz_w_lewo()
r.idz_w_prawo()
print(r.pokaz_gdzie_jestes())

