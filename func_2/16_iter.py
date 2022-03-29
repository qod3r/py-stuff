import sys


words = dict()
counter = 0

try:
    while True:
        l = sys.stdin.readline().split()
        
        for i, v in enumerate(l):
            v = v.strip('.,')
            if v not in words and v[0].isupper():
                words.update({v: counter + i})
        counter += i + 1
        
except KeyboardInterrupt:
    print()    
    for i, v in enumerate(sorted(words, key=str.lower)):
        print(f"{v} - {words[v]}")

