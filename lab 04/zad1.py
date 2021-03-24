plik = open("zad1.txt","w+")
for x in range(1,100,1):
    if(x%4==0):
        plik.writelines(str(x))
        plik.writelines("\n")