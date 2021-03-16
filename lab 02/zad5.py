x = int(input("podaj a \n")) 
if x > 10 and x < 0:
    print("liczba jest spoza przedzialu")
    k=0
else:
    k=1
y = int(input("podaj b \n"))
z = int(input("podaj c \n")) 
if x >y and y>z and k==1 :
    print("warujek jest spelniony")
else:
    print("wszystkie warunki nie sa spelnione")