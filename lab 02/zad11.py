d=int(input("liczba < 9 i > 3 \n"))
f=1
u=int(d/2)
for x in range(d,u,-1):
    print(" "*int(x-u)+ "o"*f)
    f+=2
if(d%2!=0):
    f-=4
    for j in range(2,u+2,1):
        print(" "*j+ "o"*f)
        f-=2 
else:
    f-=2
    for j in range(1,u+1,1):
        print(" "*j+ "o"*f)
        f-=2