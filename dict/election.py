lines = int(input())

results = dict()

for _ in range(lines):
    k, v = input().split(" ")
    
    if k not in results:
        results.update({k: int(v)})
    else:
        results.update({k: results[k] + int(v)})
        
print(dict(sorted(results.items())))