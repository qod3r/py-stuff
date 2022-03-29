l = list(input().split())

print(*sorted(l, key=str.lower), sep=" ")