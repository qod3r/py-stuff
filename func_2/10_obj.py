def same(func, l):
    mapped = list(map(func, l))
    # print(mapped)
    return all(x == mapped[0] for x in mapped)

v = [0, 2, 10, 6]

print("same" if same(lambda x: x % 2, v) else "diff")
