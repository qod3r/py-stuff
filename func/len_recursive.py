def r_len(l):
    if l:
        return 1 + r_len(l[1:])
    return 0

print(r_len([1, 2, 3, 4]))
print(r_len([1]*10))