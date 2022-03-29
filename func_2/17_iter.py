l = list(map(int, input().split()))
m = [l]

for i in range(1, len(l)):
    m.append(list(map(int, input().split())))

print("YES" if all(sum(i) == sum(j) for i in zip(*m) for j in m) else "NO")
