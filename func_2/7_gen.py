def cyrillic():
    for i in range(32):
        if i == 6:
            yield chr(1238)
        yield chr(1040 + i)

print(*[i for i in cyrillic()])
