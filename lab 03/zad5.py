def x(a1,a2):
    if(a1==a2):
        return "Proste równoległe"
    elif(a1*a2==-1):
        return "Proste prostopadłe"
    else:
        return "Proste nie są ani równoległe ani prostopadłe"

print(x(3,-1/3))