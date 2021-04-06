class Ciag:
    def __init__(self, ciag):
        self.ciag = ciag
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index==len(self.ciag):
            raise StopIteration
        
        if(isinstance(self.ciag,str)):
            if self.ciag[self.index] in "aeiouy" or self.ciag[self.index] in "AEIOUY":
                return self.ciag[self.index]
        else:
            return "To nie jest string"
            
g = Ciag("Jakub")
for x in g:
    print(x)







