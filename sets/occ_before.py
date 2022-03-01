s = list(map(int, input().split(" ")))
seen = []

for v in s:
    print("YES" if v in seen else "NO")
    seen.append(v)
