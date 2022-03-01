s = input().split(" ")
n = list(map(int, s))

for i, v in enumerate(n):
    if i == 0:
        continue
    
    if (v > 0 and n[i-1] > 0) or (v < 0 and n[i-1] < 0):
        print(n[i-1], v)
        break