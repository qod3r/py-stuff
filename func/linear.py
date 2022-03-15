def linear(l):
    if l == []:
        return l
    if isinstance(l[0], list):
        return linear(l[0]) + linear(l[1:])
    return l[:1] + linear(l[1:])

print(*linear([[1], [[[2]]], 3, 4]))