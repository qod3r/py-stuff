s = input().split(" ")

res = []

for e in s:
    if e not in res:
        res.append(e)
        
print(res)