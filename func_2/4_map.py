l = [i for i in range(15, 25)]

# map
print(*map(lambda x: x/2, filter(lambda y: y > 17, l)))


# comprehension
print(*[i/2 for i in l if i > 17])