l = list(map(int, input().split()))

print(*sorted(l, key=abs, reverse=True))
