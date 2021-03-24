with open("zad3.txt", "r+") as plik:
    for x in range(1,11,1):
        plik.write(str(x))
        plik.write("\n")

with open("zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")