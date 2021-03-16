x = {"Mleko":"2zł",
"Ser": "3zł",
"soja": "200zł","złoto":"sztuki","diamenty":"sztuki"}
g={ key for key , value in x.items() if value=="sztuki" }
print("sklep")
print(x)
print("sztuki")
print(g)