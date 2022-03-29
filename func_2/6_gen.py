def sqr_fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a ** 2
        a, b = b, a + b

print(*sqr_fib(7))