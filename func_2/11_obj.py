def print_op(func, row=9, col=9):
    m = [[func(i, j) for j in range(1, col + 1)] for i in range(1, row + 1)]
    for i in range(row):
        print(*m[i], sep="\t")

print_op(lambda x, y: x * y)