def miesiace():
    x = ["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for i in x:
        yield i

print(list(miesiace()))
