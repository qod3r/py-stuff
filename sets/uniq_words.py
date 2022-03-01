lines = int(input())
text = set()
for i in range(lines):
    text.update(set(input().split(" ")))

print(len(text)-1 if "" in text else len(text))