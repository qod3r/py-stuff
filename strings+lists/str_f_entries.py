s = input()

if "f" in s:
    start = s.find("f")
    end = s.rfind("f")
    if start != end:
        print(start, end)
    if start == end:
        print(start)
else:
    print()