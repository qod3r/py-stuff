c = []
for i in range(8):
    c.append(tuple(map(int, input().split(" "))))

print(c)

flag = True
for i in range(8):
    for j in range(i+1, 8):
        if c[i][0] == c[j][0] or c[i][1] == c[j][1] or abs(c[i][0] - c[j][0]) == abs(c[i][1] - c[j][1]):
            flag = False

if flag:
    print("NO")
else:
    print("YES")