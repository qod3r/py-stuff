def factorials(n):
    s = 1
    for i in range(1, n+1):
        s *= i
        yield s

print(*factorials(7))