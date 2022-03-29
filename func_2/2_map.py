l = [i for i in range(1, 11)]

# map
print(*map(lambda x: x/2, l))

# comprehension
print(*[i/2 for i in l])