a = input()
b = input()
flag = True

for char in a:
    if char == "@":
        flag = False
        break

if not flag:
    print(flag)
    exit()

flag = False
for char in b:
    if char == "@":
        flag = True
        break

print(flag)