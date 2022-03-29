import sys


words = dict()
counter = 0

try:
    while True:
        l = sys.stdin.readline().split()
        
        for i, v in enumerate(l):
            if v not in words and v[0].isupper():
                v = v.strip('.,')
                words.update({v: counter + i})
        counter += i + 1
        
except KeyboardInterrupt:
    print()    
    for i, v in enumerate(sorted(words, key=str.lower)):
        print(f"{v} - {words[v]}")

