n = int(input())
m = int(input())
symb = input()

print()
for line in range(1, n + 1):
    print(symb, end="")
    if line == 1 or line == n:
        print(symb * (m - 2), end="")
    else:
        print(" " * (m - 2) * len(symb), end="")
    print(symb, end="")
    print()