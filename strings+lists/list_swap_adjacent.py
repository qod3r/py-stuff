s = input().split(" ")

for i in range(1, len(s), 2):
    if i >= len(s):
        break
    
    s[i], s[i-1] = s[i-1], s[i]
print(s)