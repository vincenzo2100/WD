import random
matrix = [[random.randrange(1,10,1) for x in range(4)] for y in range(4)]
for i in range(0,4,1):
    print(matrix[i][i])