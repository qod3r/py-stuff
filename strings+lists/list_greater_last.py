s = input().split(" ")
n = list(map(int, s))

for i, v in enumerate(n):
    if i == 0:
        continue
    if v > n[i-1]:
        print(v, end=" ")
print()