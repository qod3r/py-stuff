lines = int(input())
syn = dict()

for _ in range(lines):
    a, b = input().split(" ")
    syn.update({a: b})
    syn.update({b: a})

query = input()

print("\t", end="")
print(syn[query])