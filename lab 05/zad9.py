def s(ciag):
        for x in range(len(ciag)-1,-1,-1):
                if ciag[x] in "aeiouy" or  ciag[x] in "AEIOUY":
                    yield ciag[x]
g = s("Jakub")
print(next(g))
print(next(g))












