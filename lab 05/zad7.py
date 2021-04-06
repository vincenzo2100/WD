class Parzysty:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        if self.index %2==0:
            return self.data[self.index]

g = Parzysty("123")
for x in g:
    print(x)

