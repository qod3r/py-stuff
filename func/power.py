def power(a, n):
    p = 1
    for _ in range(n):
        p *= a
    return p

print(power(5, 3))
print(power(2, 10))