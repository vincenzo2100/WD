def fib(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
        yield a

         
print(list(fib(10)))