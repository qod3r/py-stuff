l = [i for i in range(1, 11)]


# filter
print(*filter(lambda x: x < 5, l))

# comprehension
print(*[i for i in l if i < 5])